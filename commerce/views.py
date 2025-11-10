from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse

from commerce.models import AccessCode


@csrf_protect
def register_view(request):
    """إنشاء حساب جديد مع التحقق من رمز الوصول"""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        access_code = request.POST.get("access_code")

        # ✅ تحقق من الرمز
        try:
            access = AccessCode.objects.get(code=access_code)
            if access.used >= access.limit:
                messages.error(request, "هذا الرمز استخدم الحد المسموح.")
                return redirect("register")
        except AccessCode.DoesNotExist:
            messages.error(request, "الرمز غير صحيح!")
            return redirect("register")

        # ✅ إنشاء مستخدم جديد
        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود مسبقًا!")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # ✅ زيادة عدّاد الرمز بعد نجاح الإنشاء
        access.used += 1
        access.save()

        login(request, user)
        messages.success(request, f"تم إنشاء الحساب بنجاح يا {username}! ✅")
        return redirect("dashboard")  # غيّرها حسب مسارك

    return render(request, "commerce/register.html")


@csrf_protect
def login_view(request):
    """تسجيل دخول المستخدم"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول! 😎🔥")
            return redirect("dashboard")  # غيّر حسب مسار الدااشبورد
        else:
            messages.error(request, "البيانات غير صحيحة!")

    return render(request, "commerce/login.html")


def validate_code(request, code):
    """
    يتحقق من صلاحية الرمز ويقوم بزيادة عدد الاستخدامات عند النجاح.
    """
    try:
        access = AccessCode.objects.get(code=code)
        if access.used < access.limit:
            access.used += 1
            access.save()
            return JsonResponse({'valid': True, 'remaining': access.limit - access.used})
        else:
            return JsonResponse({'valid': False, 'reason': 'limit_reached'})
    except AccessCode.DoesNotExist:
        return JsonResponse({'valid': False, 'reason': 'not_found'})

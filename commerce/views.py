from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

# ✅ تسجيل مستخدم جديد
@csrf_protect
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # ✅ تحقق من التكرار
        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم بالفعل!")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "البريد الإلكتروني مستخدم بالفعل!")
            return redirect("register")

        # ✅ إنشاء المستخدم
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        messages.success(request, f"تم إنشاء الحساب بنجاح يا {username}! ✅")
        return redirect("home")

    return render(request, "commerce/register.html")


# ✅ تسجيل الدخول
@csrf_protect
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول ✅")
            return redirect("home")
        else:
            messages.error(request, "البيانات غير صحيحة!")

    return render(request, "commerce/login.html")


# ✅ تسجيل الخروج
def logout_view(request):
    logout(request)
    messages.success(request, "تم تسجيل الخروج بنجاح ✅")
    return redirect("home")

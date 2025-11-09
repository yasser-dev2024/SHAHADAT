from django.http import JsonResponse
from .models import AccessCode

def validate_code(request, code):
    """
    يتحقق من صلاحية الرمز ويقوم بزيادة عدد الاستخدامات عند النجاح.
    """
    try:
        access = AccessCode.objects.get(code=code)
        if access.used < access.limit:
            # الرمز صالح — زيادة عدد الاستخدامات
            access.used += 1
            access.save()
            return JsonResponse({'valid': True, 'remaining': access.limit - access.used})
        else:
            # الرمز تجاوز الحد
            return JsonResponse({'valid': False, 'reason': 'limit_reached'})
    except AccessCode.DoesNotExist:
        return JsonResponse({'valid': False, 'reason': 'not_found'})

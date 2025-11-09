from django.db import models

class AccessCode(models.Model):
    code = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name="الرمز"
    )
    limit = models.PositiveIntegerField(
        default=20, 
        verbose_name="عدد الشهادات المسموح بها"
    )
    used = models.PositiveIntegerField(
        default=0, 
        verbose_name="المستخدم منها"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="تاريخ الإنشاء"
    )

    class Meta:
        verbose_name = "رمز وصول"
        verbose_name_plural = "رموز الوصول"

    def __str__(self):
        return f"{self.code} ({self.used}/{self.limit})"

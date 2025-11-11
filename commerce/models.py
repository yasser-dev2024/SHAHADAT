from django.db import models
from django.conf import settings

# ✅ موديل رمز الوصول — كما هو بدون لمس
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


# ✅ موديل السلة — إضافة جديدة بدون التأثير على السابق
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    certificate = models.ForeignKey(
        'certificates.CertificateTemplate',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "عنصر في السلة"
        verbose_name_plural = "عناصر السلة"

    def __str__(self):
        return f"{self.user.username} - {self.certificate.title} ({self.quantity})"

    @property
    def total_price(self):
        return self.quantity * 3  # ✅ كل شهادة = 3 ريال سعودي

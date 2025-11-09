from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField(
        max_length=200, 
        verbose_name="اسم الموقع"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="تاريخ الإنشاء"
    )

    class Meta:
        verbose_name = "إعداد الموقع"
        verbose_name_plural = "إعدادات الموقع"

    def __str__(self):
        return self.site_name

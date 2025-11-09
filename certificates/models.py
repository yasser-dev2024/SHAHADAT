from django.db import models

class CertificateCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم التصنيف")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")

    class Meta:
        verbose_name = "تصنيف الشهادات"
        verbose_name_plural = "تصنيفات الشهادات"

    def __str__(self):
        return self.name


class CertificateTemplate(models.Model):
    category = models.ForeignKey(
        CertificateCategory,
        on_delete=models.CASCADE,
        related_name="templates",
        verbose_name="التصنيف",
        null=True,
        blank=True
    )
    title = models.CharField(max_length=100, verbose_name="عنوان القالب")
    background = models.ImageField(upload_to="certificates/", verbose_name="صورة الخلفية")

    class Meta:
        verbose_name = "قالب شهادة"
        verbose_name_plural = "قوالب الشهادات"

    def __str__(self):
        return self.title

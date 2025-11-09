from django.contrib import admin
from .models import CertificateTemplate, CertificateCategory

@admin.register(CertificateCategory)
class CertificateCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(CertificateTemplate)
class CertificateTemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)

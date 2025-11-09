from django.contrib import admin
from .models import AccessCode

@admin.register(AccessCode)
class AccessCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "limit", "used", "created_at")
    search_fields = ("code",)
    list_filter = ("created_at",)

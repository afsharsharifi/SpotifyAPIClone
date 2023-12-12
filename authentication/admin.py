from django.contrib import admin

from .models import OTP


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created_at", "expire_at")
    ordering = ("-created_at",)

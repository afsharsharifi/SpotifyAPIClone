from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = ("__str__", "first_name", "last_name", "email", "is_active", "created_at")
    list_filter = ("is_email_verified", "role", "is_active", "is_superuser")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("-created_at",)
    readonly_fields = ("last_seen", "created_at", "updated_at", "last_login")
    fieldsets = (
        (None, {"fields": ("email", "is_email_verified", "password")}),
        ("اطلاعات شخصی", {"fields": ("first_name", "last_name", "role", "image")}),
        ("تاریخ ها", {"fields": ("created_at", "updated_at", "last_login", "last_seen")}),
        ("دسترسی ها", {"fields": ("groups", "is_active", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "role", "email", "is_email_verified", "password1", "password2"),
            },
        ),
    )

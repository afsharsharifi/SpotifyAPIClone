from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = ("__str__", "first_name", "last_name", "verified_phone", "is_active", "created_at")
    list_filter = ("is_active", "is_superuser", "is_admin")
    search_fields = ("first_name", "last_name", "verified_phone")
    ordering = ("-created_at",)
    readonly_fields = ("last_seen", "created_at", "updated_at", "last_login")
    fieldsets = (
        (None, {"fields": ("verified_phone", "password")}),
        ("اطلاعات شخصی", {"fields": ("first_name", "last_name")}),
        ("تاریخ ها", {"fields": ("created_at", "updated_at", "last_login", "last_seen")}),
        ("دسترسی ها", {"fields": ("groups", "is_active", "is_admin", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "verified_phone", "password1", "password2"),
            },
        ),
    )


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("__str__", "fullname")


@admin.register(models.UserIP)
class UserIPAdmin(admin.ModelAdmin):
    list_display = ("__str__", "user_ip")

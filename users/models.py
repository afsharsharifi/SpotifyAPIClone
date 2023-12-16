from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from extensions import path_manager
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150, verbose_name="نام")
    last_name = models.CharField(max_length=150, verbose_name="نام خانوادگی")
    phone = models.CharField(max_length=11, unique=True, verbose_name="شماره تلفن")
    is_phone_verified = models.BooleanField(default=False, verbose_name="تایید شماره تلفن")
    is_admin = models.BooleanField(default=False, verbose_name="مدیریت")
    is_active = models.BooleanField(default=False, verbose_name="فعال")
    last_seen = models.DateTimeField(null=True, blank=True, editable=False, verbose_name="آخرین بازدید")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser

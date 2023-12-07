from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from extensions import path_manager
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOISES = [
        ("admin", "مدیر"),
        ("artist", "هنرمند"),
        ("user", "کاربر"),
    ]
    first_name = models.CharField(max_length=150, verbose_name="نام")
    last_name = models.CharField(max_length=150, verbose_name="نام خانوادگی")
    email = models.EmailField(unique=True, verbose_name="ایمیل")
    is_email_verified = models.BooleanField(default=False, verbose_name="تایید ایمیل")
    image = models.ImageField(upload_to=path_manager.create_profile_image_path, null=True, blank=True, verbose_name="تصویر")
    role = models.CharField(max_length=6, choices=ROLE_CHOISES, verbose_name="نوع کاربر")
    is_active = models.BooleanField(default=False, verbose_name="فعال")
    last_seen = models.DateTimeField(null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
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

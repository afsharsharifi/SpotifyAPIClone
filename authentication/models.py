from django.db import models
from django.utils import timezone


class OTP(models.Model):
    phone = models.CharField(max_length=11, unique=True, verbose_name="شماره همراه")
    otp_code = models.CharField(max_length=10, null=True, verbose_name="کد یکبار مصرف")
    created_at = models.DateTimeField(auto_now=True, verbose_name="درخواست", editable=False)
    expire_at = models.DateTimeField(verbose_name="انقضا", editable=False)

    class Meta:
        verbose_name = "کد یکبار مصرف"
        verbose_name_plural = "کدهای یکبار مصرف"

    def __str__(self):
        return self.phone

    def save(self, *args, **kwargs):
        self.expire_at = timezone.now() + timezone.timedelta(minutes=2)
        return super().save(*args, **kwargs)

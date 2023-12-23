from django.db import models

from users.models import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews", verbose_name="کاربر")
    comment = models.TextField(verbose_name="نظر")

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظر ها"

    def __str__(self):
        return self.user

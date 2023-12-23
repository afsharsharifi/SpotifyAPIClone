from django.db import models
from extensions.path_manager import create_songs_file_path

from users.models import Artist, User, UserIP


class Genre(models.Model):
    name = models.CharField(max_length=150, verbose_name="نام")

    class Meta:
        verbose_name = "سبک"
        verbose_name_plural = "سبک ها"

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.TextField(verbose_name="نام")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs", verbose_name="خواننده")
    genre = models.ForeignKey(Genre, related_name="songs", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="سبک")
    viewers_by_ip = models.ManyToManyField(UserIP, default="192.168.0.1", blank=True, related_name="videos", verbose_name="بازدیدکنندگان بر اساس IP")
    file_320 = models.FileField(verbose_name="کیفیت 320", upload_to=create_songs_file_path, null=True, blank=True)
    file_128 = models.FileField(verbose_name="کیفیت 128", upload_to=create_songs_file_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")

    class Meta:
        verbose_name = "آهنگ"
        verbose_name_plural = "آهنگ ها"

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", verbose_name="کاربر")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="likes", verbose_name="آهنگ")
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.song.name

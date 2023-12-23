from django.contrib import admin
from . import models


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name")


@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name", "genre")


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("__str__",)

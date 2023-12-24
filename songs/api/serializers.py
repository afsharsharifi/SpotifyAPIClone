from rest_framework import serializers

from ..models import Genre, Like, Song


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")
        read_only_fields = ("id",)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("id", "user", "song")
        read_only_fields = ("id", "user")


class SongCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("id", "name", "artist", "genre", "viewers_by_ip", "file_320", "file_128", "created_at", "updated_at")
        read_only_fields = ("id", "viewers_by_ip", "created_at", "updated_at")

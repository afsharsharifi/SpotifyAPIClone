from rest_framework import serializers

from users.api.serializers import ArtistSerializer

from ..models import Genre, Like, Song

from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes


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


class SongRetrieveSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    genre = GenreSerializer()
    views = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ("id", "name", "artist", "genre", "views", "likes", "file_320", "file_128", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")

    @extend_schema_field(OpenApiTypes.INT)
    def get_views(self, obj):
        return obj.viewers_by_ip.all().count()

    @extend_schema_field(OpenApiTypes.INT)
    def get_likes(self, obj):
        return obj.likes.all().count()


class SongCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("id", "name", "artist", "genre", "file_320", "file_128", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")

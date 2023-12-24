from rest_framework import serializers

from ..models import User, Artist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "requested_phone", "verified_phone", "password", "is_admin", "is_active", "last_seen", "created_at", "updated_at")
        read_only_fields = ("id", "last_seen", "created_at", "updated_at")
        extra_kwargs = {
            "requested_phone": {"max_length": 11, "min_length": 11},
            "verified_phone": {"max_length": 11, "min_length": 11},
            "password": {"write_only": True, "min_length": 8},
        }


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", "fullname", "bio", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")

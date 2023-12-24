from rest_framework import serializers

from ..models import Artist, User


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

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            requested_phone=validated_data["requested_phone"],
            verified_phone=validated_data["verified_phone"],
            password=validated_data["password"],
        )
        user.is_admin = validated_data["is_admin"]
        user.is_active = validated_data["is_active"]
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "requested_phone", "verified_phone", "is_admin", "is_active", "last_seen", "created_at", "updated_at")
        read_only_fields = ("id", "last_seen", "created_at", "updated_at")
        extra_kwargs = {
            "requested_phone": {"max_length": 11, "min_length": 11},
            "verified_phone": {"max_length": 11, "min_length": 11},
        }


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", "fullname", "bio", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")

from rest_framework import serializers

from authentication.api.serializers import UserRegisterSerializer

from ..models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ("id", "user", "comment", "created_at", "updated_at")
        read_only_fields = ("id", "user", "created_at", "updated_at")

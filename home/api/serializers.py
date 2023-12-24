from rest_framework import serializers

from ..models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "user", "comment", "created_at", "updated_at")
        read_only_fields = ("id", "user", "created_at", "updated_at")

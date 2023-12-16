from rest_framework import serializers

from users.models import User


class PhoneNumberSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, min_length=11, required=True)


class OTPPhoneNumberSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, min_length=11, required=True)
    otp_code = serializers.CharField(max_length=6, min_length=6, required=True)


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone", "password")
        read_only_fields = ("id",)
        extra_kwargs = {
            "phone": {"max_length": 11, "min_length": 11},
            "password": {"write_only": True, "min_length": 8},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"],
            phone=validated_data["phone"],
        )
        return user

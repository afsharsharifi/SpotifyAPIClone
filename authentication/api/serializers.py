from rest_framework import serializers


class PhoneNumberSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, required=True)


class OTPPhoneNumberSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, required=True)
    otp_code = serializers.CharField(max_length=6, required=True)

from rest_framework import serializers


class AuthUserResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()


class LoginResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
    user = AuthUserResponseSerializer()


class RegisterResponseSerializer(serializers.Serializer):
    user = AuthUserResponseSerializer()


class TokenValidationResponseSerializer(serializers.Serializer):
    valid = serializers.BooleanField(default=True)
    user = AuthUserResponseSerializer()

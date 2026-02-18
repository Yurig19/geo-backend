from rest_framework import serializers


class DomainErrorResponseSerializer(serializers.Serializer):
    error = serializers.BooleanField(read_only=True)
    code = serializers.CharField(read_only=True)
    message = serializers.CharField(read_only=True)

from rest_framework import serializers


class ValidationErrorResponseSerializer(serializers.Serializer):
    error = serializers.BooleanField(
        default=True,
        read_only=True,
        help_text="Sempre true para respostas de erro",
    )

    code = serializers.CharField(
        default="VALIDATION_ERROR",
        read_only=True,
        help_text="Código padronizado indicando erro de validação",
    )

    message = serializers.CharField(
        default="Erro na requisição",
        read_only=True,
        help_text="Mensagem descritiva do erro",
    )

    details = serializers.JSONField(
        read_only=True,
        help_text="Objeto contendo erros de validação por campo",
    )

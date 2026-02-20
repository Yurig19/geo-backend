from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema

from src.core.swagger_domain import DomainErrorResponseSerializer

from ..serializers.auth_response_serializer import TokenValidationResponseSerializer


class TokenValidationView(APIView):
    @extend_schema(
        tags=["Auth"],
        responses={
            200: TokenValidationResponseSerializer,
            401: DomainErrorResponseSerializer,
        },
        description="Valida o token JWT e retorna os dados do usuário autenticado",
    )
    def get(self, request: Request) -> Response:
        user = request.user

        return Response(
            {
                "valid": True,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
            },
            status=status.HTTP_200_OK,
        )

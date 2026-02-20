from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema

from src.core.swagger_domain import DomainErrorResponseSerializer
from src.core.swagger_schemas import ValidationErrorResponseSerializer

from ...infrastructure.repositories.user_repository import UserRepository
from ...application.use_cases.register_user import RegisterUserUseCase
from ...application.dtos.user_response import UserResponseDTO
from ...application.dtos.register_response_dto import RegisterResponseDTO
from ..serializers.register_serializer import RegisterSerializer
from ..serializers.auth_response_serializer import RegisterResponseSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        tags=["Auth"],
        request=RegisterSerializer,
        auth=[],
        responses={
            201: RegisterResponseSerializer,
            400: ValidationErrorResponseSerializer,
            409: DomainErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Cria um novo usuário",
    )
    def post(self, request: Request) -> Response:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        repository = UserRepository()
        use_case = RegisterUserUseCase(repository)

        user = use_case.execute(**serializer.validated_data)

        user_dto = UserResponseDTO(
            id=user.id,
            username=user.username,
            email=user.email,
        )

        response_dto = RegisterResponseDTO(user=user_dto)

        return Response(
            {
                "user": response_dto.user.__dict__,
            },
            status=status.HTTP_201_CREATED,
        )

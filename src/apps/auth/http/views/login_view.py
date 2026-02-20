from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema

from src.core.swagger_domain import DomainErrorResponseSerializer
from src.core.swagger_schemas import ValidationErrorResponseSerializer

from ...infrastructure.repositories.user_repository import UserRepository
from ...application.use_cases.login_use_case import LoginUserUseCase
from ...application.dtos.user_response import UserResponseDTO
from ...application.dtos.login_response_dto import LoginResponseDTO
from ..serializers.login_serializer import LoginSerializer
from ..serializers.auth_response_serializer import LoginResponseSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        tags=["Auth"],
        request=LoginSerializer,
        auth=[],
        responses={
            200: LoginResponseSerializer,
            400: ValidationErrorResponseSerializer,
            401: DomainErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Autentica usuário e retorna tokens JWT",
    )
    def post(self, request: Request) -> Response:
        print(request.data)
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        repository = UserRepository()
        use_case = LoginUserUseCase(repository)

        user = use_case.execute(**serializer.validated_data)

        refresh = RefreshToken.for_user(user)

        user_dto = UserResponseDTO(
            id=user.id,
            username=user.username,
            email=user.email,
        )

        response_dto = LoginResponseDTO(
            access=str(refresh.access_token),
            refresh=str(refresh),
            user=user_dto,
        )

        return Response(
            {
                "access": response_dto.access,
                "refresh": response_dto.refresh,
                "user": response_dto.user.__dict__,
            },
            status=status.HTTP_200_OK,
        )

from rest_framework.request import Request
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.views import APIView

from src.core.swagger_domain import DomainErrorResponseSerializer
from src.core.swagger_schemas import (
    ValidationErrorResponseSerializer,
)
from ...places.application.use_cases.create_place import CreatePlaceUseCase
from ...places.application.dtos.create_place_dto import CreatePlaceDTO
from ...places.application.dtos.place_response_dto import PlaceResponseDTO

from .serializers import PlaceSerializer

from rest_framework.permissions import IsAuthenticated


class PlaceCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Places"],
        request=PlaceSerializer,
        responses={
            201: PlaceSerializer,
            400: ValidationErrorResponseSerializer,
            409: DomainErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Cria um novo local geográfico",
    )
    def post(self, request: Request) -> Response:
        serializer = PlaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = CreatePlaceDTO(**serializer.validated_data)

        use_case = CreatePlaceUseCase()
        result: PlaceResponseDTO = use_case.execute(dto)

        return Response(
            {
                "id": result.id,
                "name": result.name,
                "latitude": result.latitude,
                "longitude": result.longitude,
            },
            status=status.HTTP_201_CREATED,
        )

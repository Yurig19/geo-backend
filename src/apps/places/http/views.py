from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.core.swagger_domain import DomainErrorResponseSerializer
from src.core.swagger_schemas import ValidationErrorResponseSerializer

from ..application.dtos.create_place_point_dto import CreatePlacePointDTO
from ..application.dtos.land_use_area_query_dto import LandUseAreaQueryDTO
from ..application.dtos.land_use_area_response_dto import LandUseAreaResponseDTO
from ..application.dtos.land_use_options_response_dto import LandUseOptionsResponseDTO
from ..application.dtos.place_point_response_dto import PlacePointResponseDTO
from ..application.use_cases.create_place_point import CreatePlacePointUseCase
from ..application.use_cases.get_land_use_area import GetLandUseAreaUseCase
from ..application.use_cases.list_land_use_options import ListLandUseOptionsUseCase
from ..application.use_cases.list_place_points import ListPlacePointsUseCase
from .serializers import (
    LandUseAreaQuerySerializer,
    LandUseAreaResponseSerializer,
    LandUseOptionsResponseSerializer,
    PlacePointCreateSerializer,
    PlacePointResponseSerializer,
)


class PlacePointView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Places"],
        responses={
            200: PlacePointResponseSerializer(many=True),
            500: DomainErrorResponseSerializer,
        },
        description="Lista todos os pontos salvos",
    )
    def get(self, request: Request) -> Response:
        use_case = ListPlacePointsUseCase()
        results: list[PlacePointResponseDTO] = use_case.execute()

        return Response(
            [result.__dict__ for result in results],
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        tags=["Places"],
        request=PlacePointCreateSerializer,
        responses={
            201: PlacePointResponseSerializer,
            400: ValidationErrorResponseSerializer,
            404: DomainErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Salva um ponto e infere o uso do solo via geometria",
    )
    def post(self, request: Request) -> Response:
        serializer = PlacePointCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = CreatePlacePointDTO(**serializer.validated_data)
        use_case = CreatePlacePointUseCase()
        result: PlacePointResponseDTO = use_case.execute(dto)

        return Response(result.__dict__, status=status.HTTP_201_CREATED)


class LandUseOptionsView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Places"],
        responses={
            200: LandUseOptionsResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Lista os possíveis usos do solo (land_use_description)",
    )
    def get(self, request: Request) -> Response:
        use_case = ListLandUseOptionsUseCase()
        result: LandUseOptionsResponseDTO = use_case.execute()
        return Response(result.__dict__, status=status.HTTP_200_OK)


class LandUseAreaView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Places"],
        parameters=[
            OpenApiParameter(
                name="land_use_description",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Descrição do uso do solo",
            ),
        ],
        responses={
            200: LandUseAreaResponseSerializer,
            400: ValidationErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Retorna a área total (m²) para um uso do solo",
    )
    def get(self, request: Request) -> Response:
        serializer = LandUseAreaQuerySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        dto = LandUseAreaQueryDTO(**serializer.validated_data)
        use_case = GetLandUseAreaUseCase()
        result: LandUseAreaResponseDTO = use_case.execute(dto)

        return Response(result.__dict__, status=status.HTTP_200_OK)

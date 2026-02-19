from uuid import UUID

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.core.swagger_domain import DomainErrorResponseSerializer
from src.core.swagger_schemas import ValidationErrorResponseSerializer

from ...application.dtos.create_product_dto import CreateProductDTO
from ...application.dtos.delete_product_dto import DeleteProductDTO
from ...application.dtos.get_product_by_id_dto import GetProductByIdDTO
from ...application.dtos.product_response_dto import ProductResponseDTO
from ...application.dtos.stock_operation_dto import StockOperationDTO
from ...application.dtos.update_product_dto import UpdateProductDTO
from ...application.use_cases.add_stock import AddStockUseCase
from ...application.use_cases.create_product import CreateProductUseCase
from ...application.use_cases.delete_product import DeleteProductUseCase
from ...application.use_cases.get_product_by_id import GetProductByIdUseCase
from ...application.use_cases.list_products import ListProductsUseCase
from ...application.use_cases.remove_stock import RemoveStockUseCase
from ...application.use_cases.update_product import UpdateProductUseCase
from ...infrastructure.repositories.product_repository import ProductRepository
from ..serializers.product_serializer import (
    ProductCreateSerializer,
    ProductResponseSerializer,
    ProductUpdateSerializer,
    StockOperationSerializer,
)


class ProductCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Products"],
        responses={
            200: ProductResponseSerializer(many=True),
            500: DomainErrorResponseSerializer,
        },
        description="Lista todos os produtos",
    )
    def get(self, request: Request) -> Response:
        repository = ProductRepository()
        use_case = ListProductsUseCase(repository)
        results = use_case.execute()

        return Response(
            [result.__dict__ for result in results],
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        tags=["Products"],
        request=ProductCreateSerializer,
        responses={
            201: ProductResponseSerializer,
            400: ValidationErrorResponseSerializer,
            409: DomainErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Cria um novo produto",
    )
    def post(self, request: Request) -> Response:
        serializer = ProductCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = CreateProductDTO(**serializer.validated_data)

        repository = ProductRepository()
        use_case = CreateProductUseCase(repository)
        result: ProductResponseDTO = use_case.execute(dto)

        return Response(
            result.__dict__,
            status=status.HTTP_201_CREATED,
        )


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Products"],
        responses={
            200: ProductResponseSerializer,
            404: DomainErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Busca um produto por id",
    )
    def get(self, request: Request, product_id: UUID) -> Response:
        dto = GetProductByIdDTO(product_id=product_id)

        repository = ProductRepository()
        use_case = GetProductByIdUseCase(repository)
        result: ProductResponseDTO = use_case.execute(dto)

        return Response(
            result.__dict__,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        tags=["Products"],
        request=ProductUpdateSerializer,
        responses={
            200: ProductResponseSerializer,
            400: ValidationErrorResponseSerializer,
            404: DomainErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Atualiza um produto",
    )
    def put(self, request: Request, product_id: UUID) -> Response:
        serializer = ProductUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = UpdateProductDTO(product_id=product_id, **serializer.validated_data)

        repository = ProductRepository()
        use_case = UpdateProductUseCase(repository)
        result: ProductResponseDTO = use_case.execute(dto)

        return Response(
            result.__dict__,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        tags=["Products"],
        responses={
            204: None,
            404: DomainErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Remove um produto",
    )
    def delete(self, request: Request, product_id: UUID) -> Response:
        dto = DeleteProductDTO(product_id=product_id)

        repository = ProductRepository()
        use_case = DeleteProductUseCase(repository)
        use_case.execute(dto)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductAddStockView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Products"],
        request=StockOperationSerializer,
        responses={
            200: ProductResponseSerializer,
            400: ValidationErrorResponseSerializer,
            404: DomainErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Adiciona estoque a um produto",
    )
    def patch(self, request: Request, product_id: UUID) -> Response:
        serializer = StockOperationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = StockOperationDTO(product_id=product_id, **serializer.validated_data)

        repository = ProductRepository()
        use_case = AddStockUseCase(repository)
        result: ProductResponseDTO = use_case.execute(dto)

        return Response(
            result.__dict__,
            status=status.HTTP_200_OK,
        )


class ProductRemoveStockView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Products"],
        request=StockOperationSerializer,
        responses={
            200: ProductResponseSerializer,
            400: ValidationErrorResponseSerializer,
            404: DomainErrorResponseSerializer,
            409: DomainErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Remove estoque de um produto",
    )
    def patch(self, request: Request, product_id: UUID) -> Response:
        serializer = StockOperationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = StockOperationDTO(product_id=product_id, **serializer.validated_data)

        repository = ProductRepository()
        use_case = RemoveStockUseCase(repository)
        result: ProductResponseDTO = use_case.execute(dto)

        return Response(
            result.__dict__,
            status=status.HTTP_200_OK,
        )

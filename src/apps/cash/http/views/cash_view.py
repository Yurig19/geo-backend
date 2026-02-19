from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.core.swagger_domain import DomainErrorResponseSerializer
from src.core.swagger_schemas import ValidationErrorResponseSerializer

from ...application.dtos.cash_movement_response_dto import CashMovementResponseDTO
from ...application.dtos.cash_summary_response_dto import CashSummaryResponseDTO
from ...application.dtos.create_cash_movement_dto import CreateCashMovementDTO
from ...application.use_cases.get_cash_summary import GetCashSummaryUseCase
from ...application.use_cases.list_cash_transactions import ListCashTransactionsUseCase
from ...application.use_cases.list_expenses import ListExpensesUseCase
from ...application.use_cases.register_cash_movement import RegisterCashMovementUseCase
from ...infrastructure.repositories.cash_repository import CashRepository
from ..serializers.cash_serializer import (
    CashMovementCreateSerializer,
    CashMovementResponseSerializer,
    CashMovementTypeQuerySerializer,
    CashSummaryResponseSerializer,
)


class CashMovementView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Cash"],
        responses={
            200: CashMovementResponseSerializer(many=True),
            500: DomainErrorResponseSerializer,
        },
        description="Lista todas as transações de caixa",
    )
    def get(self, request: Request) -> Response:
        repository = CashRepository()
        use_case = ListCashTransactionsUseCase(repository)
        results = use_case.execute()

        return Response(
            [result.__dict__ for result in results],
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        tags=["Cash"],
        request=CashMovementCreateSerializer,
        responses={
            201: CashMovementResponseSerializer,
            400: ValidationErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Registra movimentação de caixa (entrada/saída)",
    )
    def post(self, request: Request) -> Response:
        serializer = CashMovementCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = CreateCashMovementDTO(**serializer.validated_data)
        repository = CashRepository()
        use_case = RegisterCashMovementUseCase(repository)
        result: CashMovementResponseDTO = use_case.execute(dto)

        return Response(result.__dict__, status=status.HTTP_201_CREATED)


class CashSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Cash"],
        responses={
            200: CashSummaryResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Retorna o resumo do caixa",
    )
    def get(self, request: Request) -> Response:
        repository = CashRepository()
        use_case = GetCashSummaryUseCase(repository)
        result: CashSummaryResponseDTO = use_case.execute()

        return Response(result.__dict__, status=status.HTTP_200_OK)


class ExpenseListView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Cash"],
        parameters=[
            OpenApiParameter(
                name="type",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Tipo da movimentação: INCOME ou EXPENSE",
            ),
        ],
        responses={
            200: CashMovementResponseSerializer(many=True),
            400: ValidationErrorResponseSerializer,
            500: DomainErrorResponseSerializer,
        },
        description="Lista movimentações por tipo via query param",
    )
    def get(self, request: Request) -> Response:
        serializer = CashMovementTypeQuerySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        movement_type = serializer.validated_data["type"]

        repository = CashRepository()
        use_case = ListExpensesUseCase(repository)
        results = use_case.execute(movement_type=movement_type)

        return Response(
            [result.__dict__ for result in results], status=status.HTTP_200_OK
        )

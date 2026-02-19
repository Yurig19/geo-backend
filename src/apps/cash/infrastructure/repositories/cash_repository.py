from decimal import Decimal

from django.db.models import Sum

from ..models.cash_transaction import CashTransactionModel


class CashRepository:

    def create_transaction(
        self,
        movement_type: str,
        amount: Decimal,
        description: str,
    ) -> CashTransactionModel:
        return CashTransactionModel.objects.create(
            movement_type=movement_type,
            amount=amount,
            description=description,
        )

    def total_by_type(self, movement_type: str) -> Decimal:
        result = CashTransactionModel.objects.filter(movement_type=movement_type).aggregate(
            total=Sum("amount")
        )
        return result["total"] or Decimal("0")

    def list_by_type(self, movement_type: str) -> list[CashTransactionModel]:
        return list(
            CashTransactionModel.objects.filter(movement_type=movement_type).order_by(
                "-created_at"
            )
        )

    def list_all(self) -> list[CashTransactionModel]:
        return list(CashTransactionModel.objects.all().order_by("-created_at"))

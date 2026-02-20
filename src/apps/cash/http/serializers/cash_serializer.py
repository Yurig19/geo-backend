from decimal import Decimal

from rest_framework import serializers

from ...infrastructure.models.cash_transaction import CashMovementType


class CashMovementCreateSerializer(serializers.Serializer):
    movement_type = serializers.ChoiceField(choices=CashMovementType.choices)
    amount = serializers.DecimalField(
        max_digits=12, decimal_places=2, min_value=Decimal("0.01")
    )
    description = serializers.CharField(required=False, allow_blank=True, default="")


class CashMovementResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    movement_type = serializers.CharField(read_only=True)
    amount = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    description = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)


class CashSummaryResponseSerializer(serializers.Serializer):
    total_income = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    total_expense = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    balance = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)


class CashMovementTypeQuerySerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=CashMovementType.choices)

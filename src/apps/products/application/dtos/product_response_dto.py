from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any
from uuid import UUID


@dataclass
class ProductResponseDTO:
    id: UUID
    name: str
    unit_price: Decimal | float
    quantity: int
    total_value: Decimal | float
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_model(cls, product: Any) -> "ProductResponseDTO":
        return cls(
            id=product.id,
            name=product.name,
            unit_price=product.unit_price,
            quantity=product.quantity,
            total_value=product.total_value,
            created_at=product.created_at,
            updated_at=product.updated_at,
        )

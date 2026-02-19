from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID


@dataclass
class CashMovementResponseDTO:
    id: UUID
    movement_type: str
    amount: Decimal
    description: str
    created_at: datetime

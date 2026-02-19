from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CreateCashMovementDTO:
    movement_type: str
    amount: Decimal
    description: str

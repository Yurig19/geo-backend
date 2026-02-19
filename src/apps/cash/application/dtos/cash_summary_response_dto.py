from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CashSummaryResponseDTO:
    total_income: Decimal
    total_expense: Decimal
    balance: Decimal

from dataclasses import dataclass
from uuid import UUID


@dataclass
class StockOperationDTO:
    product_id: UUID
    amount: int

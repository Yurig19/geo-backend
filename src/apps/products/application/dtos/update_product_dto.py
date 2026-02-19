from dataclasses import dataclass
from uuid import UUID


@dataclass
class UpdateProductDTO:
    product_id: UUID
    name: str
    unit_price: float

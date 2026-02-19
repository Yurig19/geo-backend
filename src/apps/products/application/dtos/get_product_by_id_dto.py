from dataclasses import dataclass
from uuid import UUID


@dataclass
class GetProductByIdDTO:
    product_id: UUID

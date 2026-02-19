from dataclasses import dataclass
from uuid import UUID


@dataclass
class DeleteProductDTO:
    product_id: UUID

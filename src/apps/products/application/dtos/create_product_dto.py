from dataclasses import dataclass


@dataclass
class CreateProductDTO:
    name: str
    unit_price: float
    quantity: int

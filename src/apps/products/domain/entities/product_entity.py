from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from ..exceptions.products import InsufficientStockException


@dataclass
class Product:
    name: str
    unit_price: float
    quantity: int

    id: UUID = field(default_factory=uuid4)
    total_value: float = field(init=False)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self) -> None:
        self._validate()
        self._recalculate_total()

    def _validate(self) -> None:
        if self.unit_price < 0:
            raise ValueError("O preço não pode ser negativo")

        if self.quantity < 0:
            raise ValueError("A quantidade não pode ser negativa")

    def _recalculate_total(self) -> None:
        self.total_value = self.unit_price * self.quantity
        self.updated_at = datetime.utcnow()

    def add_stock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Quantidade para adicionar deve ser maior que zero")

        self.quantity += amount
        self._recalculate_total()

    def remove_stock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Quantidade para remover deve ser maior que zero")

        if amount > self.quantity:
            raise InsufficientStockException()

        self.quantity -= amount
        self._recalculate_total()

    def update_price(self, new_price: float) -> None:
        if new_price < 0:
            raise ValueError("Preço não pode ser negativo")

        self.unit_price = new_price
        self._recalculate_total()

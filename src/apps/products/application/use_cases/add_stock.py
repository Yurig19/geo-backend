from ..dtos.product_response_dto import ProductResponseDTO
from ..dtos.stock_operation_dto import StockOperationDTO
from ...domain.exceptions.products import ProductNotFoundException

from ...infrastructure.repositories.product_repository import ProductRepository


class AddStockUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, data: StockOperationDTO) -> ProductResponseDTO:
        product = self.repository.get_by_id(data.product_id)

        if not product:
            raise ProductNotFoundException()

        product.quantity += data.amount
        product.total_value = product.unit_price * product.quantity

        updated = self.repository.save(product)
        return ProductResponseDTO.from_model(updated)

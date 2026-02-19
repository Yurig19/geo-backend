from ..dtos.product_response_dto import ProductResponseDTO
from ..dtos.update_product_dto import UpdateProductDTO
from ...domain.exceptions.products import ProductNotFoundException

from ...infrastructure.repositories.product_repository import ProductRepository


class UpdateProductUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, data: UpdateProductDTO) -> ProductResponseDTO:
        product = self.repository.get_by_id(data.product_id)

        if not product:
            raise ProductNotFoundException()

        product.name = data.name
        product.unit_price = data.unit_price
        product.total_value = data.unit_price * product.quantity

        updated = self.repository.save(product)
        return ProductResponseDTO.from_model(updated)

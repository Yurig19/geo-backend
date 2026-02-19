from ..dtos.delete_product_dto import DeleteProductDTO
from ...domain.exceptions.products import ProductNotFoundException

from ...infrastructure.repositories.product_repository import ProductRepository


class DeleteProductUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, data: DeleteProductDTO) -> None:
        product = self.repository.get_by_id(data.product_id)

        if not product:
            raise ProductNotFoundException()

        self.repository.delete(product)

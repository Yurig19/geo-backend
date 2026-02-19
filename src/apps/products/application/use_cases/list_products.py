from ..dtos.product_response_dto import ProductResponseDTO
from ...infrastructure.repositories.product_repository import ProductRepository


class ListProductsUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self) -> list[ProductResponseDTO]:
        products = self.repository.list_all()
        return [ProductResponseDTO.from_model(product) for product in products]

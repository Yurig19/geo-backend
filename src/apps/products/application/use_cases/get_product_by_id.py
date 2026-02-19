from ..dtos.get_product_by_id_dto import GetProductByIdDTO
from ..dtos.product_response_dto import ProductResponseDTO
from ...domain.exceptions.products import ProductNotFoundException
from ...infrastructure.repositories.product_repository import ProductRepository


class GetProductByIdUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, data: GetProductByIdDTO) -> ProductResponseDTO:
        product = self.repository.get_by_id(data.product_id)

        if not product:
            raise ProductNotFoundException()

        return ProductResponseDTO.from_model(product)

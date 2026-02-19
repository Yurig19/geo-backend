from ..dtos.create_product_dto import CreateProductDTO
from ..dtos.product_response_dto import ProductResponseDTO
from ...domain.entities.product_entity import Product
from ...infrastructure.repositories.product_repository import ProductRepository


class CreateProductUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, data: CreateProductDTO) -> ProductResponseDTO:
        product = Product(
            name=data.name,
            unit_price=data.unit_price,
            quantity=data.quantity,
        )

        print(product)

        created = self.repository.create(product)
        return ProductResponseDTO.from_model(created)

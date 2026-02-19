from typing import Optional
from uuid import UUID

from ..models.product import ProductModel
from ...domain.entities.product_entity import Product


class ProductRepository:

    def create(self, product: Product) -> ProductModel:
        return ProductModel.objects.create(
            id=product.id,
            name=product.name,
            unit_price=product.unit_price,
            quantity=product.quantity,
            total_value=product.total_value,
        )

    def get_by_id(self, product_id: UUID) -> Optional[ProductModel]:
        return ProductModel.objects.filter(id=product_id).first()

    def list_all(self) -> list[ProductModel]:
        return list(ProductModel.objects.all().order_by("-created_at"))

    def delete(self, product: ProductModel) -> None:
        product.delete()

    def save(self, product: ProductModel) -> ProductModel:
        product.save()
        return product

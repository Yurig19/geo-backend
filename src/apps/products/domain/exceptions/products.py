from src.core.exceptions import DomainException
from src.core.error_code.products import ProductErrorCode


class ProductNotFoundException(DomainException):
    def __init__(self) -> None:
        super().__init__(
            message="Produto não encontrado",
            code=ProductErrorCode.NOT_FOUND,
        )


class ProductAlreadyExistsException(DomainException):
    def __init__(self) -> None:
        super().__init__(
            message="Já existe um produto com esse identificador/nome",
            code=ProductErrorCode.ALREADY_EXISTS,
        )


class InvalidProductPriceException(DomainException):
    def __init__(self) -> None:
        super().__init__(
            message="Preço do produto inválido",
            code=ProductErrorCode.INVALID_PRICE,
        )


class InvalidProductQuantityException(DomainException):
    def __init__(self) -> None:
        super().__init__(
            message="Quantidade do produto inválida",
            code=ProductErrorCode.INVALID_QUANTITY,
        )


class InsufficientStockException(DomainException):
    def __init__(self) -> None:
        super().__init__(
            message="Estoque insuficiente",
            code=ProductErrorCode.INSUFFICIENT_STOCK,
        )


class InvalidStockOperationException(DomainException):
    def __init__(self) -> None:
        super().__init__(
            message="Operação de estoque inválida",
            code=ProductErrorCode.STOCK_OPERATION_INVALID,
        )

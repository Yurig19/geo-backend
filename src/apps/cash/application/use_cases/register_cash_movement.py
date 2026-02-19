from ...application.dtos.cash_movement_response_dto import CashMovementResponseDTO
from ...application.dtos.create_cash_movement_dto import CreateCashMovementDTO
from ...infrastructure.repositories.cash_repository import CashRepository


class RegisterCashMovementUseCase:

    def __init__(self, repository: CashRepository):
        self.repository = repository

    def execute(self, data: CreateCashMovementDTO) -> CashMovementResponseDTO:
        transaction = self.repository.create_transaction(
            movement_type=data.movement_type,
            amount=data.amount,
            description=data.description,
        )
        return CashMovementResponseDTO(
            id=transaction.id,
            movement_type=transaction.movement_type,
            amount=transaction.amount,
            description=transaction.description,
            created_at=transaction.created_at,
        )

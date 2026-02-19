from ...application.dtos.cash_movement_response_dto import CashMovementResponseDTO
from ...infrastructure.repositories.cash_repository import CashRepository


class ListCashTransactionsUseCase:

    def __init__(self, repository: CashRepository):
        self.repository = repository

    def execute(self) -> list[CashMovementResponseDTO]:
        transactions = self.repository.list_all()
        return [
            CashMovementResponseDTO(
                id=transaction.id,
                movement_type=transaction.movement_type,
                amount=transaction.amount,
                description=transaction.description,
                created_at=transaction.created_at,
            )
            for transaction in transactions
        ]

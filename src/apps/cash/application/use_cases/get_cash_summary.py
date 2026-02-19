from ...application.dtos.cash_summary_response_dto import CashSummaryResponseDTO
from ...infrastructure.models.cash_transaction import CashMovementType
from ...infrastructure.repositories.cash_repository import CashRepository


class GetCashSummaryUseCase:

    def __init__(self, repository: CashRepository):
        self.repository = repository

    def execute(self) -> CashSummaryResponseDTO:
        total_income = self.repository.total_by_type(CashMovementType.INCOME)
        total_expense = self.repository.total_by_type(CashMovementType.EXPENSE)

        return CashSummaryResponseDTO(
            total_income=total_income,
            total_expense=total_expense,
            balance=total_income - total_expense,
        )

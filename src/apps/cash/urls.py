from django.urls import path

from .http.views.cash_view import CashMovementView, CashSummaryView, ExpenseListView

urlpatterns = [
    path("cash/transactions/", CashMovementView.as_view(), name="cash-transactions"),
    path("cash/expenses/", ExpenseListView.as_view(), name="cash-expenses"),
    path("cash/", CashSummaryView.as_view(), name="cash-summary"),
]

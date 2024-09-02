from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryListView.as_view(), name="category list"),
    path('income/create/', IncomeCreateView.as_view(), name='income-create'),
    path('expense/create/', ExpenseCreateView.as_view(), name='expense-create'),
]

# Sample request data for IncomeCreateView
# {
#     "incomeID": 5,
#     "date": "2024-09-01",
#     "incomeCategory": "Rent",
#     "amount": 10002.0,
#     "discount": 2.0,
#     "total": 10000.0,
#     "addedBy": "admin@gmail.com",
#     "paidBy": "user1@gmail.com",
# }
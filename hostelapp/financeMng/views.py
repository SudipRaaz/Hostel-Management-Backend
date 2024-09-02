from rest_framework import generics
from rest_framework.views import APIView
from .models import CategoryList, Income, Expense
from .serializers import CategoryListSerializer, IncomeSerializer, ExpenseSerializer

class CategoryListView(generics.ListAPIView):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer

class IncomeCreateView(generics.CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class ExpenseCreateView(generics.CreateAPIView):
    queryset= Expense.objects.all()
    serializer_class = ExpenseSerializer
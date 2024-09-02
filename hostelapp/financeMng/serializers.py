from rest_framework import serializers
from .models import CategoryList, Income, Expense

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryList
        fields = '__all__'  # Alternatively, specify fields explicitly like ['categoryID', 'category', 'active', 'type']

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'  # Alternatively, specify fields explicitly like ['incomeID', 'incomeTitle', 'amount', 'categoryID', 'date']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'  # Alternatively, specify fields explicitly like ['incomeID', 'incomeTitle', 'amount', 'categoryID', 'date']

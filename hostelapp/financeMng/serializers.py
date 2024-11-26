from rest_framework import serializers

from seatMng.models import seatMng
from .models import CategoryList, TransactionTable, BillGenerate, Expense

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryList
        fields = '__all__'  # Alternatively, specify fields explicitly like ['categoryID', 'category', 'active', 'type']

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionTable
        fields = '__all__'  # Alternatively, specify fields explicitly like ['incomeID', 'incomeTitle', 'amount', 'categoryID', 'date']
        

class BillGenerateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillGenerate
        fields = ['seatID_finance', 'billedAmount', 'discountAmount', 'billedMonth', 'billDescription']
        # fields = '__all__'

    def validate(self, data):
        # Check if billedAmount is missing and apply a default (based on seatMng priceRate if needed)
        if 'billedAmount' not in data or data['billedAmount'] is None:
            seat = data.get('seatID_finance')
            if seat and seat.priceRate:
                data['billedAmount'] = seat.priceRate
            else:
                raise serializers.ValidationError("billedAmount or seat priceRate is required.")
        
        return data
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'  # Alternatively, specify fields explicitly like ['incomeID', 'incomeTitle', 'amount', 'categoryID', 'date']

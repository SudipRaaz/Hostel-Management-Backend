from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from seatMng.models import seatMng
from .models import CategoryList, IncomingPayments,BilledPayment, Expense
from .serializers import CategoryListSerializer, IncomeSerializer, BilledPaymentSerializer, ExpenseSerializer

class CategoryListView(generics.ListAPIView):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer

class IncomeCreateView(generics.CreateAPIView):
    queryset = IncomingPayments.objects.all()
    serializer_class = IncomeSerializer
    
class GenerateBillView(APIView):
    def post(self, request):
        # Initialize the serializer with the request data
        serializer = BilledPaymentSerializer(data=request.data)

        # Ensure validation is performed before accessing validated_data
        if serializer.is_valid():
            # Try to access the validated data safely
            seat_id = serializer.validated_data.get('seatID_finance')  # type: ignore
            billed_month = serializer.validated_data.get('billedMonth')  # type: ignore
            discount = serializer.validated_data.get('discountAmount', 0)  # type: ignore
            description = serializer.validated_data.get('billDescription', '')  # type: ignore

            # Ensure seatID and other required fields exist
            if seat_id is None or billed_month is None:
                return Response({"error": "Required fields are missing (billed month or seatID)"}, status=status.HTTP_400_BAD_REQUEST)

            # Fetch seatMng object to get the priceRate if billedAmount not provided
            try:
                seat = seatMng.objects.get(seatID=seat_id.seatID)
            except seatMng.DoesNotExist:
                return Response({"error": "Seat not found"}, status=status.HTTP_404_NOT_FOUND)

            # Use provided billedAmount, or fall back to seatMng's priceRate
            billed_amount = serializer.validated_data.get('billedAmount', seat.priceRate)  # type: ignore

            # Calculate total billed amount by subtracting any discount
            total_billed_amount = billed_amount - discount

            # Create the bill record by passing the seat ID, not the entire object
            new_bill = BilledPayment.objects.create(
                seatID_finance=seat,  # Use seatID instead of the entire seat object
                billedAmount=total_billed_amount,
                billedMonth=billed_month,
                billDescription=description,
                discountAmount=discount
            )

            return Response({
                "message": "Bill generated successfully",
                "bill_id": new_bill.billID,
                "billed_amount": total_billed_amount,
                "status": new_bill.status,
                "billed_month": new_bill.billedMonth
            }, status=status.HTTP_201_CREATED)

        # Return errors if validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, billID, **kwargs):
        billDetails = BilledPayment.objects.filter(billID=billID).first()
        
        if billDetails is None:
            return Response({"error": "Bill not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BilledPaymentSerializer(billDetails)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, billID, **kwargs):
        bill = BilledPayment.objects.get(billID=billID)
        if bill is not None:
            bill.delete()
            return Response({"success": "Bill Deleted Successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "Bill not found"}, status=status.HTTP_404_NOT_FOUND)



class ExpenseCreateView(generics.CreateAPIView):
    queryset= Expense.objects.all()
    serializer_class = ExpenseSerializer
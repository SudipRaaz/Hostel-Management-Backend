from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import seatMng, Rooms, seatNumber
from django.db import models 
from .serializers import SeatMngSerializer, RoomSerializer, SeatNumberSerializer

class SeatMngCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Extract seatMng data from request
        seat_mng_data = request.data.get('seat')
        seat_number_value = seat_mng_data.get('seatNumber')  # SeatNumber value from request

        # Check if seatNumber exists in the seatNumber table
        try:
            seat_number_instance = seatNumber.objects.get(seatNumber=seat_number_value)
        except seatNumber.DoesNotExist:
            return Response({'error': 'seatNumber does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve the relevant roomID using seatNumber
        room_instance = seat_number_instance.roomNumber  # This gives us the relevant Rooms instance

        # Increment the occupancy in the Rooms model
        if room_instance.occupancy < room_instance.totalSeats:
            room_instance.occupancy += 1
            room_instance.save()
        else:
            return Response({'error': 'Room occupancy is full'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new seatMng entry
        seat_mng_data['seatNumber'] = seat_number_instance.pk  # Add seatNumber foreign key
        seat_mng_data['RoomNumber'] =  room_instance.roomNumber
        seat_serializer = SeatMngSerializer(data=seat_mng_data)

        if seat_serializer.is_valid():
            seat_serializer.save()  # Save the seatMng instance
            return Response({
                'seatMng': seat_serializer.data,
                'room': RoomSerializer(room_instance).data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(seat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SeatMngListInactiveAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Calculate total seats across all rooms
        total_seats = Rooms.objects.aggregate(total=models.Sum('totalSeats'))['total'] or 0

        # Calculate total occupancy across all Rooms
        total_occupancy = Rooms.objects.aggregate(occupied=models.Sum('occupancy'))['occupied'] or 0

        # Calculate available seats
        available_seats = total_seats - total_occupancy

        data = {
            'total_seats': total_seats,
            'occupied_seats': total_occupancy,
            'available_seats': available_seats
        }
        return Response(data)
    
class CreateRoom(generics.CreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer


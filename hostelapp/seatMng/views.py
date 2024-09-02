from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import seatMng, Rooms
from django.db import models 
from .serializers import SeatSerializer, RoomSerializer

class SeatMngCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SeatSerializer(data=request.data)
        if serializer.is_valid():
            # creates the room objects directly as seatSerializer instances the roomID with Rooms model as it is used as foreign key,
            # and same instance of Room is return along with roomID 
            room = serializer.validated_data['roomID']
            # this will increase the occupancy count by +1 for the room assigned
            if room.occupancy <= room.totalSeats:
                room.occupancy += 1
                room.save()
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Room is full'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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


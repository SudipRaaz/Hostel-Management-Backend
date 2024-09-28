from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.generics import ListAPIView
from .models import seatMng, Rooms, seatNumber
from django.db import models 
from .serializers import SeatMngSerializer, RoomSerializer, SeatNumberSerializer

# create seat with their respective room ID
class AllocateSeatToUser(APIView):
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
    
    
class SeatManagement(APIView):
    def get(self, request, *args, **kwargs):
        seatNumber_object = seatNumber.objects.all()

        available_seats = []
        unoccupied_seat = seatNumber_object.filter(occupiedStatus = False)

        serializer = SeatNumberSerializer(data = unoccupied_seat, many= True)
        
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)
                # Your code logic here

class UnoccupiedSeatsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Get all unoccupied seats
        rooms = Rooms.objects.all()
        
        room_seats = []
        
        for room in rooms:
            unoccupiedSeat = seatNumber.objects.filter(roomNumber = room.roomID, occupiedStatus = False) # type: ignore
            seatSerializer = SeatNumberSerializer(unoccupiedSeat, many= True)
            room_seats.append({
                'roomID': room.roomID,
                'unoccupiedSeat': seatSerializer.data}
            )
        # Return the RoomID and list of unoccupied seatID
        return Response(room_seats, status=status.HTTP_200_OK)

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

# room management
class RoomManagement(APIView):
    # Create a room
    def post(self, request, *args, **kwargs):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get all rooms
    def get(self, request, pk=None, *args, **kwargs):
        # If `pk` is provided, return seats for the specific room
        if pk is not None:
            try:
                seat_number_objects = seatNumber.objects.filter(roomNumber=pk)
                if not seat_number_objects.exists():
                    return Response({'error': 'No seats found for the provided room.'}, status=status.HTTP_404_NOT_FOUND)
                
                serializer = SeatNumberSerializer(seat_number_objects, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Rooms.DoesNotExist:
                return Response({'error': 'Room not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Otherwise, return all rooms
        rooms = Rooms.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    # Update a room
    def put(self, request, pk, *args, **kwargs):
        try:
            room = Rooms.objects.get(pk=pk)
        except Rooms.DoesNotExist:
            return Response({'error': 'Room not found'}, status=status.HTTP_404_NOT_FOUND)
        # room serializer
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a room
    def delete(self, request, pk, *args, **kwargs):
        try:
            room = Rooms.objects.get(pk=pk)
        except Rooms.DoesNotExist:
            return Response({'error': 'Room not found'}, status=status.HTTP_404_NOT_FOUND)

        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
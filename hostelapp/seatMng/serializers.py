from rest_framework import serializers
from .models import seatMng, Rooms, seatNumber

class SeatMngSerializer(serializers.ModelSerializer):
    class Meta:
        model = seatMng
        fields = ('seatID', 'priceRate', 'active', 'seatNumber', 'RoomNumber')

class SeatNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = seatNumber
        fields = ('seatNumber','roomID','seatPriceRate', 'occupiedStatus' )

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('roomID','roomName', 'roomNumber', 'totalSeats' ,'roomType',)
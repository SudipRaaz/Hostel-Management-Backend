from rest_framework import serializers
from .models import seatMng, Rooms, seatNumber

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = seatMng
        fields = ('seatID', 'priceRate', 'active', 'seatNumber',)

class SeatNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = seatNumber
        fields = ('seatNumber','roomID')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('roomID','roomName', 'roomNumber', 'occupancy','totalSeats' ,'roomType',)
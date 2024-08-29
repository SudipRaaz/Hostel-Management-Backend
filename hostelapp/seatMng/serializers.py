from rest_framework import serializers
from .models import seatMng, Rooms

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = seatMng
        fields = ('seatID', 'priceRate', 'active', 'seatNumber', 'roomID')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('roomID','roomName', 'roomNumber', 'occupancy','totalSeats' ,'roomType',)
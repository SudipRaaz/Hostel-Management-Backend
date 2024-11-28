from rest_framework import serializers
from .models import seatMng, Rooms, seatNumber

class SeatMngSerializer(serializers.ModelSerializer):
    # Include related field data
    # seatNumber = serializers.CharField(source='seatNumberPK.seatNumber', read_only=True) 
    class Meta:
        model = seatMng
        fields = ('seatID', 'priceRate', 'active', 'seatNumber', 'RoomNumber')

class SeatNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = seatNumber
        fields = ('seatNumber','roomNumber','seatPriceRate', 'occupiedStatus' )

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('roomID','roomName', 'roomNumber', 'totalSeats' ,'roomType',)
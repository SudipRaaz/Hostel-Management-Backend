from django.db import models

# from userMng.models import User

class Rooms(models.Model):
    roomID = models.AutoField(primary_key=True)
    roomName = models.CharField(max_length=100, null=True)
    roomNumber = models.IntegerField(unique=True)
    occupancy = models.IntegerField(default=0)
    totalSeats = models.IntegerField()
    roomType = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.roomName} (Room {self.roomNumber})"
    
class seatNumber(models.Model):
    seatNumber = models.IntegerField(primary_key=True)
    roomNumber = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='seatRoomNumber')
    seatPriceRate = models.FloatField(default=0.0)
    occupiedStatus = models.BooleanField(default=False)
    
class seatMng(models.Model):
    seatID = models.AutoField(primary_key=True)
    priceRate = models.FloatField()
    active = models.BooleanField(default=True)
    RoomNumber = models.IntegerField()
    seatNumber = models.ForeignKey(seatNumber, on_delete=models.DO_NOTHING, related_name="seat_number")
    # userID = models.ForeignKey(User, on_delete=models.PROTECT, related_name="assigned_user")


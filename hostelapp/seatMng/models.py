from django.db import models
import datetime

class Rooms(models.Model):
    roomID = models.AutoField(primary_key=True)
    roomName = models.CharField(max_length=100, null=True)
    roomNumber = models.IntegerField(unique=True)
    occupancy = models.IntegerField(default=0)
    totalSeats = models.IntegerField()
    roomType = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.roomName} (Room {self.roomNumber})"

class seatMng(models.Model):
    seatID = models.AutoField(primary_key=True)
    priceRate = models.FloatField()
    active = models.BooleanField(default=True)
    seatNumber = models.IntegerField(null=True)
    dateJoined = models.DateTimeField(default=datetime.datetime.now())
    roomID = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='seatRoom')

    def __str__(self):
        return f"Seat {self.seatID} in {self.roomID.roomName}"

from django.urls import path
from .views import *

urlpatterns = [
    
    path('create-seat', SeatMngCreateAPIView.as_view(), name="create for new hosteler" ),
    
    # room management
    path('room', RoomManagement.as_view(), name="Room Management"),
    path('room/<int:pk>', RoomManagement.as_view(), name="Room Management"),
    
    # dashboard management
    path('seats-available', SeatMngListInactiveAPIView.as_view(), name="create for new hosteler" ),
    path('unoccupied-seats/', UnoccupiedSeatsAPIView.as_view(), name='unoccupied_seats'),
]

# payload parameters for seats creation
# {
#     "seat": {
#         "priceRate": 1500.00,
#         "active": true,
#         "seatNumber": 101  # Assuming seatNumber 101 exists
#     }
# }

# payload parameters for create-rooms
# {
#   "roomName": "Deluxe Room",
#   "roomNumber": 101,
#   "occupancy": 0,
#   "totalSeats": 4,
#   "roomType": "Double"
# }
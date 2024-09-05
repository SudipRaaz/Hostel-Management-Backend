from django.urls import path
from . import views

urlpatterns = [
    path('seats', views.SeatMngCreateAPIView.as_view(), name="create for new hosteler" ),
    path('seats-available', views.SeatMngListInactiveAPIView.as_view(), name="create for new hosteler" ),
    # This line of code is defining a URL pattern using Django's path() function. When a user
    # navigates to the URL "create-rooms" in the application, Django will call the `as_view()` method
    # on the `CreateRoom` view class from the `views` module. The `name` parameter is providing a
    # unique name for this URL pattern, which can be used to refer to it in the application's code.
    path('create-rooms', views.CreateRoom.as_view(), name="create-room" )
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
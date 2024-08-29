from django.urls import path
from . import views

urlpatterns = [
    path('seats', views.SeatMngCreateAPIView.as_view(), name="create for new hosteler" ),
    path('seats-available', views.SeatMngListInactiveAPIView.as_view(), name="create for new hosteler" ),
    path('create-rooms', views.CreateRoom.as_view(), name="create-room" )
]
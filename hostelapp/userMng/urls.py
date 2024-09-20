from django.urls import path
from . import views

urlpatterns = [
    # register user
    path('register/', views.RegisterViews.as_view(), name="register user"),
    # login users
    path('login/', views.LoginViews.as_view(), name="user login"),
    # search users
    path('userview/', views.UserView.as_view(), name="user view - get user details from JWT token"),
    path('user/<str:email>/', views.RegisterViews.as_view(), name='get user details with email search '),
    # get all users
    path('user/', views.UserListView.as_view(), name='get user details with email search '),
    # user logout
    path('logout/', views.logout.as_view(), name="user logout"),
]

# register user with seat
# {
#     "seat": {
#         "priceRate": 1500.00,
#         "active": true,
#         "seatNumber": 1
#     },
#     "user": {
#         "name": "John Doe",
#         "email": "user1@example.com",
#         "password": "securepassword",
#         "gender": "Male",
#         "phone_number": "1234567890",
#         "address": "123 Street Name",
#         "date_of_birth": "2000-01-01"
#     }
# }


from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterViews.as_view(), name="register user"),
    path('login/', views.LoginViews.as_view(), name="user login"),
    path('userview/', views.UserView.as_view(), name="user view"),
    path('logout/', views.logout.as_view(), name="user logout"),
	# path('register', views.UserRegister.as_view(), name='register'),
	# path('login', views.UserLogin.as_view(), name='login'),
	# path('logout', views.UserLogout.as_view(), name='logout'),
	# path('user', views.UserView.as_view(), name='user'),
]

# register user with seat
# {
#     "seat": {
#         "priceRate": 1500.00,
#         "active": true,
#         "seatNumber": 101,
#         "roomID": 1
#     },
#     "user": {
#         "name": "John Doe",
#         "email": "user@example.com",
#         "password": "securepassword",
#         "gender": "Male",
#         "phone_number": "1234567890",
#         "address": "123 Street Name",
#         "date_of_birth": "2000-01-01"
#     }
# }

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
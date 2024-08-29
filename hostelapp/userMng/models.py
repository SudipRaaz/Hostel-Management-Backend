from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	email = models.EmailField(max_length=255, unique=True)
	password = models.CharField(max_length=255)
	gender = models.CharField(max_length=255,  null=True)
	phone_number = models.CharField(max_length=255, null=True)
	address = models.CharField(max_length=255, null=True)
	date_of_birth = models.DateField(null=True)
	username = None
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
    
from django.contrib.auth.models import BaseUserManager
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

from seatMng.models import seatMng


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('seatID_id', 1)

        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    first_name = None
    last_name = None
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField()
    admissionDate = models.DateField(default=datetime.date.today)
    seatID = models.ForeignKey(seatMng,on_delete=models.PROTECT, related_name='seatID_Number')
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager() # type: ignore




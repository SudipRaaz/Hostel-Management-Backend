import datetime
from django.db import models

# Create your models here.
class CategoryList(models.Model):
    categoryID = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.category
    
class Expense(models.Model):
    expenseID = models.AutoField(primary_key=True)
    expenseTitle = models.CharField(max_length=50)
    expenseAmount = models.FloatField()
    description = models.TextField(null=True)
    date = models.DateField(default=datetime.datetime.now)
    category = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.expenseTitle


class Income(models.Model):
    incomeID = models.AutoField(primary_key=True)
    incomeCategory = models.CharField(max_length=50)
    amount = models.FloatField(max_length=10)
    discount = models.FloatField(max_length=10)
    total = models.FloatField(max_length=10)

class Vendors(models.Model):
    name = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    active = models.BooleanField(default=True)
    vendorType = models.CharField(max_length=20)

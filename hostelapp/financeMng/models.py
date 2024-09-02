import datetime
from django.db import models
from userMng.models import User

# Create your models here.
class CategoryList(models.Model):
    categoryID = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50) # category title
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
    date = models.DateField(default=datetime.date.today)
    incomeCategory = models.CharField(max_length=50)
    description = models.TextField(max_length=100, null=True)
    amount = models.FloatField(max_length=10)
    discount = models.FloatField(max_length=10)
    total = models.FloatField(max_length=10)
    addedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name="added_by")
    paidBy = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="paidBy")

class Vendors(models.Model):
    name = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    active = models.BooleanField(default=True)
    vendorType = models.CharField(max_length=20)

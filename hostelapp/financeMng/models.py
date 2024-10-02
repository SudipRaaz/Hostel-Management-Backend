import datetime
from django.db import models
from seatMng.models import seatMng
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


class IncomingPayments(models.Model):
    ipaymentID = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today)
    incomeCategory = models.CharField(max_length=50)
    description = models.TextField(max_length=100, null=True)
    paidAmount = models.FloatField(max_length=10, default=0)
    discountAmount = models.FloatField(max_length=10, default=0)
    dueAmount = models.FloatField(max_length=10, default=0)
    # paidUsing = models.CharField(max_length=20, null=True)
    # addedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name="added_by")
    paidBy = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="paidBy")

class BillGenerate(models.Model):
    paymentStatus = [('Unpaid', 'Unpaid'),('Partial', 'Partial'),('Paid', 'Paid'),]
    billID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_bill")
    seatID_finance = models.ForeignKey(seatMng,on_delete=models.PROTECT, related_name='seatID_Num')
    billedAmount = models.FloatField(default=0)
    billedDate = models.DateField(default=datetime.datetime.now)
    status = models.CharField(max_length=20, choices=paymentStatus, default='Unpaid')
    billedMonth = models.CharField(max_length=50)
    billDescription = models.TextField(max_length=150, null=True)
    discountAmount = models.FloatField(null=True)
    




class Vendors(models.Model):
    name = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    active = models.BooleanField(default=True)
    vendorType = models.CharField(max_length=20)

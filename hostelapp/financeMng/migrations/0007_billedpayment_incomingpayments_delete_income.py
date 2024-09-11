# Generated by Django 5.1 on 2024-09-09 16:58

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financeMng", "0006_income_description_alter_income_date"),
        ("seatMng", "0007_remove_seatmng_roomid_alter_seatmng_seatnumber"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BilledPayment",
            fields=[
                ("billID", models.AutoField(primary_key=True, serialize=False)),
                ("billedAmount", models.FloatField()),
                ("billedDate", models.DateField(default=datetime.datetime.now)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Unpaid", "Unpaid"),
                            ("Partial", "Partial"),
                            ("Paid", "Paid"),
                        ],
                        default="Unpaid",
                        max_length=20,
                    ),
                ),
                (
                    "seatID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="seatID_Num",
                        to="seatMng.seatmng",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IncomingPayments",
            fields=[
                ("ipaymentID", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField(default=datetime.date.today)),
                ("incomeCategory", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=100, null=True)),
                ("paidAmount", models.FloatField(max_length=10)),
                ("discountAmount", models.FloatField(max_length=10)),
                ("dueAmount", models.FloatField(max_length=10)),
                ("paidUsing", models.CharField(max_length=20)),
                (
                    "paidBy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="paidBy",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Income",
        ),
    ]

# Generated by Django 5.1 on 2024-09-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financeMng", "0011_billedpayment_billedamount"),
    ]

    operations = [
        migrations.RenameField(
            model_name="billedpayment",
            old_name="seatID",
            new_name="seatID_finance",
        ),
        migrations.AlterField(
            model_name="billedpayment",
            name="billedAmount",
            field=models.FloatField(default=0),
        ),
    ]

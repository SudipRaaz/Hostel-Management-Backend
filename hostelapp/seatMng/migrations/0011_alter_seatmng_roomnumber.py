# Generated by Django 5.1 on 2024-09-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seatMng", "0010_seatmng_roomnumber_seatnumber_occupiedstatus_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seatmng",
            name="RoomNumber",
            field=models.IntegerField(),
        ),
    ]

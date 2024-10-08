# Generated by Django 5.1 on 2024-08-30 18:30

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seatMng", "0004_remove_seatmng_datejoined_alter_seatmng_seatnumber"),
        ("userMng", "0002_alter_user_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="admissionDate",
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="user",
            name="date_of_birth",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="seatID",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="seatNum",
                to="seatMng.seatmng",
            ),
            preserve_default=False,
        ),
    ]

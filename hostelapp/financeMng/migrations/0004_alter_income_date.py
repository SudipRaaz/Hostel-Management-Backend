# Generated by Django 5.1 on 2024-09-01 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financeMng", "0003_income_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="income",
            name="date",
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]

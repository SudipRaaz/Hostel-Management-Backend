# Generated by Django 5.1 on 2024-09-01 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userMng", "0004_alter_user_managers"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default="2000-02-05", max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="admissionDate",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
# Generated by Django 5.1 on 2024-08-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userMng", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="address",
            field=models.CharField(max_length=255, null=True),
        ),
    ]

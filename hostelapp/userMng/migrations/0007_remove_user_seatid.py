# Generated by Django 5.1 on 2024-09-10 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userMng", "0006_remove_user_first_name_remove_user_last_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="seatID",
        ),
    ]

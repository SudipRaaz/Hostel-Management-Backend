# Generated by Django 5.1 on 2024-09-01 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userMng", "0005_user_name_alter_user_admissiondate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="last_name",
        ),
    ]

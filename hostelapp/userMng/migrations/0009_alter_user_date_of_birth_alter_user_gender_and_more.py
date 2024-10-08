# Generated by Django 5.1 on 2024-09-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userMng", "0008_user_seatid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_of_birth",
            field=models.DateField(default="2024-08-31"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(default="Male", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(default=89849845848, max_length=255),
            preserve_default=False,
        ),
    ]

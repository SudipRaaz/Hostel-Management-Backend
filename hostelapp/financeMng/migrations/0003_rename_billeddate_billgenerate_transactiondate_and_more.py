# Generated by Django 5.1 on 2024-11-19 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("financeMng", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="billgenerate",
            old_name="billedDate",
            new_name="transactionDate",
        ),
        migrations.RenameField(
            model_name="billgenerate",
            old_name="billID",
            new_name="tranxID",
        ),
    ]

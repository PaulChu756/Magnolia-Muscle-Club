# Generated by Django 4.2.6 on 2023-10-29 03:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mmc", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="type_of_account",
            field=models.CharField(
                choices=[("Free", "Free"), ("Paid", "Paid"), ("Admin", "Admin")],
                default="Free",
                max_length=10,
            ),
        ),
    ]
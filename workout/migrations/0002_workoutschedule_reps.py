# Generated by Django 4.2.6 on 2023-11-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workout", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="workoutschedule",
            name="reps",
            field=models.IntegerField(default=10),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workout", "0002_workoutschedule_reps"),
    ]

    operations = [
        migrations.AddField(
            model_name="workoutschedule",
            name="sets",
            field=models.IntegerField(default=3),
        ),
    ]
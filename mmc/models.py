from django.db import models


# Define the Workout model with a dropdown select menu
class Workout(models.Model):
    WORKOUT_CHOICES = [
        ("Cardio", "Cardio"),
        ("Strength Training", "Strength Training"),
        ("Yoga", "Yoga"),
        # Add more workout types as needed
    ]
    name = models.CharField(max_length=100)
    workout_type = models.CharField(max_length=50, choices=WORKOUT_CHOICES)

    def __str__(self):
        return self.name


# Define the Weight model
class Weight(models.Model):
    value = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Weight: {self.value} lbs ({self.date})"


# Define the Personal Best model
class PersonalBest(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return f"Personal Best for {self.workout}"


# Create your models here.


class WorkoutSchedule(models.Model):
    workoutName = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.workoutName


class Day(models.Model):
    day_of_week = models.CharField(max_length=10)
    schedule = models.ForeignKey(WorkoutSchedule, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.schedule.workoutName} - {self.day_of_week}"


class Exercise(models.Model):
    workoutName = models.CharField(max_length=255)
    description = models.TextField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return self.workoutName

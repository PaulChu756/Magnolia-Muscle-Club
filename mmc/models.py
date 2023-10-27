from django.db import models

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

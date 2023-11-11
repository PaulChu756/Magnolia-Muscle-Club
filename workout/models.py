from django.db import models

WORKOUT_CHOICES = (
    ("Cardio", "Cardio"),
    ("Strength Training", "Strength Training"),
    ("Yoga", "Yoga"),
)


# Define the Workout model with a dropdown select menu
class Workout(models.Model):
    """Workout model."""

    name = models.CharField(max_length=100)
    workout_type = models.CharField(max_length=50, choices=WORKOUT_CHOICES)

    def __str__(self) -> str:
        return f"{self.name}"


class Weight(models.Model):
    """Weight model."""

    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add user reference
    value = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Weight: {self.value} lbs ({self.date})"


class PersonalBest(models.Model):
    """The Personal Best model."""

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return f"Personal Best for {self.workout}"


class WorkoutSchedule(models.Model):
    """Workout schedule model."""

    workoutName = models.CharField(max_length=255)
    reps = models.IntegerField(default=10)
    sets = models.IntegerField(default=3)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.workoutName}"


class Day(models.Model):
    """Day model."""

    day_of_week = models.CharField(max_length=10)
    schedule = models.ForeignKey(WorkoutSchedule, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.schedule.workoutName} - {self.day_of_week}"


class Exercise(models.Model):
    """Exercise model."""

    workoutName = models.CharField(max_length=255)
    description = models.TextField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.workoutName}"


class WorkOutVideos(models.Model):
    """Work out videos model."""

    workOutDay = models.CharField(max_length=200)
    workOutVideoLink = models.CharField(max_length=200)

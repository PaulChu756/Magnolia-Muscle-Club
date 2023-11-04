"""MMC Models."""
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser

# Define the choices first
TYPE_CHOICES = (
    ("Free", "Free"),
    ("Paid", "Paid"),
    ("Admin", "Admin"),
)

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

FITNESS_GROUP_CHOICES = (
    ("Group A", "Group A"),
    ("Group B", "Group B"),
    ("Group C", "Group C"),
)

MEAL_CHOICES = (
    ("breakfast", "Breakfast"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
    ("snacks", "Snacks"),
)

WORKOUT_CHOICES = (
    ("Cardio", "Cardio"),
    ("Strength Training", "Strength Training"),
    ("Yoga", "Yoga"),
)


class UserProfile(models.Model):
    """User Profile model."""

    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    type_of_account = models.CharField(max_length=10, choices=TYPE_CHOICES, default="Free")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)


# Define the Workout model with a dropdown select menu
class Workout(models.Model):
    """Workout model."""

    name = models.CharField(max_length=100)
    workout_type = models.CharField(max_length=50, choices=WORKOUT_CHOICES)

    def __str__(self) -> str:
        return f"{self.name}"


class Weight(models.Model):
    """Weight model."""

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


class FoodLibrary(models.Model):
    """Food library model."""

    foodDay = models.CharField(max_length=200)
    foodChoice = models.CharField(max_length=200)


class MealEntry(models.Model):
    """Meal Entry model."""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    food_item = models.CharField(max_length=100)
    calories_consumed = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s {self.meal_type} entry"


class Notification(models.Model):
    """Notification model."""

    fitness_group = models.CharField(max_length=20, choices=FITNESS_GROUP_CHOICES)
    message = models.TextField()
    sent_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="sent_notifications"
    )
    recipients = models.ManyToManyField(CustomUser, related_name="received_notifications")

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.fitness_group}"

    class Meta:
        """Meta class."""

        ordering = ["-timestamp"]


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    """Create UserProfile object when a new CustomUser signs up."""
    if sender and created:
        UserProfile.objects.create(custom_user=instance)


post_save.connect(create_profile, sender=CustomUser)

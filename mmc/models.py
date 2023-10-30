from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser


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


class UserProfile(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    type_of_account = models.CharField(max_length=10, choices=TYPE_CHOICES, default="Free")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if sender and created:
        UserProfile.objects.create(custom_user=instance)


post_save.connect(create_profile, sender=CustomUser)
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


# Create your models here.
class MealEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    meal_type = models.CharField(
        max_length=20,
        choices=[
            ("breakfast", "Breakfast"),
            ("lunch", "Lunch"),
            ("dinner", "Dinner"),
            ("snacks", "Snacks"),
        ],
    )
    food_item = models.CharField(max_length=100)
    calories_consumed = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s {self.meal_type} entry"


# Define the choices for the fitness group dropdown
FITNESS_GROUP_CHOICES = (
    ("Group A", "Group A"),
    ("Group B", "Group B"),
    ("Group C", "Group C"),
    # Add more fitness group choices as needed
)


class Notification(models.Model):
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
        ordering = ["-timestamp"]

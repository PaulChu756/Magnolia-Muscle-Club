from django.db import models

from users.models import CustomUser

MEAL_CHOICES = (
    ("breakfast", "Breakfast"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
    ("snacks", "Snacks"),
)


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

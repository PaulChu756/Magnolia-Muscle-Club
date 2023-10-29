from django.db import models

from users.models import CustomUser


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

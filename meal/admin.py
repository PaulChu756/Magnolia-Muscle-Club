from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.FoodLibrary)
admin.site.register(models.MealEntry)

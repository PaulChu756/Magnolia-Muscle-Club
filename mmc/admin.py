from django.contrib import admin

from .models import PersonalBest, Weight, Workout


@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = ["value", "date"]
    # Add any other customizations here


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ["name", "workout_type"]
    # Add any other customizations here


@admin.register(PersonalBest)
class PersonalBestAdmin(admin.ModelAdmin):
    list_display = ["workout", "value"]
    # Add any other customizations here


# @admin.register(Chart)
# class ChartAdmin(admin.ModelAdmin):
#     list_display = ["workout", "workouts_per_week"]
#     # Add any other customizations here

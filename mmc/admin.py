from django.contrib import admin

from .models import Day, Exercise, PersonalBest, Weight, Workout, WorkoutSchedule

admin.site.register(PersonalBest)
admin.site.register(Weight)
admin.site.register(Workout)

# Register your models here.
admin.site.register(WorkoutSchedule)
admin.site.register(Day)
admin.site.register(Exercise)

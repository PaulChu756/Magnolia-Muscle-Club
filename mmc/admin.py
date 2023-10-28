from django.contrib import admin

from .models import Day, Exercise, WorkoutSchedule

# Register your models here.
admin.site.register(WorkoutSchedule)
admin.site.register(Day)
admin.site.register(Exercise)

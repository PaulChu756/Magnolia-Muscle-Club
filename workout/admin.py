from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Day)
admin.site.register(models.Exercise)
admin.site.register(models.PersonalBest)
admin.site.register(models.Weight)
admin.site.register(models.Workout)

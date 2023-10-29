from django.db import models


class WorkOutVideos(models.Model):
    workOutDay = models.CharField(max_length=200)
    workOutVideoLink = models.CharField(max_length=200)

class FoodLibrary(models.Model):
    foodDay = models.CharField(max_length=200)
    foodChoice = models.CharField(max_length=200)


# Create your models here.

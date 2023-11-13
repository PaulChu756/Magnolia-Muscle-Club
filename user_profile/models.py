from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser


# TYPE_CHOICES = (
#     ("Free", "Free"),
#     ("Paid", "Paid"),
#     ("Trainer", "Trainer"),
# )

# GENDER_CHOICES = (
#     ("Male", "Male"),
#     ("Female", "Female"),
#     ("Other", "Other"),
# )


# Create your models here.
class UserProfile(models.Model):
    """User Profile model."""

    class Gender(models.IntegerChoices):
        """Gender choice class."""
        FEMALE = 1
        MALE = 2
        OTHER = 3

    #type_of_account = models.CharField(max_length=10, choices=TYPE_CHOICES, default="Free")
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=Gender.choices, default=2)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    phone = models.CharField(blank=True, null=True, default="1-123-456-7890", max_length=15)
    is_free_account = models.BooleanField(default=True)
    is_paid_account = models.BooleanField(default=False)
    is_trainer_account = models.BooleanField(default=False)


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    """Create UserProfile object when a new CustomUser signs up."""
    if sender and created:
        UserProfile.objects.create(custom_user=instance)


post_save.connect(create_profile, sender=CustomUser)

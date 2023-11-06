from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser

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


# Create your models here.
class UserProfile(models.Model):
    """User Profile model."""

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
    """Create UserProfile object when a new CustomUser signs up."""
    if sender and created:
        UserProfile.objects.create(custom_user=instance)


post_save.connect(create_profile, sender=CustomUser)

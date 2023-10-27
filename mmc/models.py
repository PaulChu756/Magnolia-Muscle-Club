from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

# UserProfile model to store additional user information
class UserProfile(models.Model):
    # Link the user profile to the built-in User model
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    # Custom fields for user profile
    type_of_account_choices = (
        ('Free', 'Free'),
        ('Paid', 'Paid'),
        ('Admin', 'Admin'),
    )
    type_of_account = models.CharField(max_length=10, choices=type_of_account_choices)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=gender_choices)

    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username


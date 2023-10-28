from django.db import models
from django.contrib.auth import get_user_model

# Define the choices first
TYPE_CHOICES = (
    ('Free', 'Free'),
    ('Paid', 'Paid'),
    ('Admin', 'Admin'),
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    type_of_account = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Free')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

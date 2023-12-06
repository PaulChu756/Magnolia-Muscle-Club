from django import forms

from . import models

ACCOUNT_CHOICES = ((0, "None"), (1, "Free"), (2, "Paid"), (3, "Trainer"))

class UserProfileUpdateForm(forms.ModelForm):
    """User profile change view."""

    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    account_type = forms.ChoiceField(choices=ACCOUNT_CHOICES, required=False)

    class Meta:
        model = models.UserProfile
        fields = ["first_name", "last_name", "gender", "age", "picture", "weight", "height", "phone"]

from django import forms
from user_profile.models import UserProfile

ACCOUNT_CHOICES = ((0, "Free"), (1, "Paid"), (2, "Trainer"))

class UserProfileUpdateForm(forms.ModelForm):
    """User profile change view."""

    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    account_type = forms.ChoiceField(choices=ACCOUNT_CHOICES, required=False)

    class Meta:
        """Meta class."""

        model = UserProfile
        fields = ["first_name", "last_name", "gender", "age", "picture", "weight", "height", "phone"]

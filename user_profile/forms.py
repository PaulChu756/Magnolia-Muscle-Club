from django import forms
from user_profile.models import UserProfile

ACCOUNT_TYPE_CHOICES = [
    ('free', 'Free'),
    ('paid', 'Paid'),
    ('trainer', 'Trainer'),
]

class UserProfileUpdateForm(forms.ModelForm):
    """User profile change view."""

    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES)

    class Meta:
        """Meta class."""

        model = UserProfile
        fields = ["first_name", "last_name", "gender", "age", "picture", "weight", "height", "phone"]

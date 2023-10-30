"""Forms for accounts app."""
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import CustomUser
from mmc.models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    """Registration form."""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = ("first_name", "last_name", "email", "password1", "password2")


class CustomUserChangeForm(UserChangeForm):
    """User profile change view."""

    class Meta:
        """Meta class."""

        model = UserProfile
        fields = ("id", "first_name", "last_name", "picture", "weight", "height", "phone", "gender")

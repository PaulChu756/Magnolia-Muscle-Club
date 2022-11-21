"""Accounts view."""
from django.urls import reverse_lazy
from django.views import generic

from users.forms import CustomUserCreationForm
from users.models import CustomUser


class SignUpView(generic.CreateView):
    """User registration view."""

    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

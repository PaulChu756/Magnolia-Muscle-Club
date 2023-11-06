"""Accounts view."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from users.forms import CustomUserCreationForm
from users.models import CustomUser


class SignUpView(CreateView):
    """User registration view."""

    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("login")
    extra_context = {"title_text": "Sign Up", "button_text": "Register"}


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """Profile detail view.

    Reason why `slug_field` and `slug_url_kwargs` are set as `None`:
    - By default, in a `DetailView`, the object of the model is retrieved from the URL parameters.
    - In this case, as the model is `CustomUser`, the object of user is retrieved from the request.

    """

    model = CustomUser
    template_name = "registration/profile.html"
    slug_field = None
    slug_url_kwarg = ""

    def get_object(self, queryset=None):
        """Owner of the object should be the current user."""
        return self.request.user

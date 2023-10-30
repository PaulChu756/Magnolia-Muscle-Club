"""Accounts view."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import CustomUser
from mmc.models import UserProfile


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


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Profile update view."""

    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "registration/profile_update.html"
    success_url = reverse_lazy("users:profile_detail")

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        userprofile = UserProfile.objects.get_or_create(
            id=10,
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            picture=form.cleaned_data["picture"],
            weight=form.cleaned_data["weight"],
            height=form.cleaned_data["height"],
            phone=form.cleaned_data["phone"],
            gender=form.cleaned_data["gender"],
            #data=form.cleaned_data["data"]
        )
        return super().form_valid(form)

    def get_object(self, queryset=None):
        """Owner of the object should be the current user."""
        return self.request.user

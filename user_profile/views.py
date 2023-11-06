from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from users.forms import CustomUserChangeForm
from users.models import CustomUser

from . import models


class UserProfileDetailView(generic.DetailView):
    model = models.UserProfile


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Profile update view."""

    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "registration/profile_update.html"
    success_url = reverse_lazy("users:profile_detail")

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        userprofile = models.UserProfile.objects.get_or_create(
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            picture=form.cleaned_data["picture"],
            weight=form.cleaned_data["weight"],
            height=form.cleaned_data["height"],
            phone=form.cleaned_data["phone"],
            gender=form.cleaned_data["gender"],
        )
        userprofile.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        """Owner of the object should be the current user."""
        return self.request.user

"""Accounts app URL Configuration."""
from django.urls import path

from users import views as users_views

app_name = "users"

urlpatterns = [
    path("signup/", users_views.SignUpView.as_view(), name="signup"),
    path("profile/", users_views.ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/update/", users_views.ProfileUpdateView.as_view(), name="profile_update"),
]

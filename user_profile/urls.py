from django.urls import path

from . import views
from user_profile import views as profile_views

app_name = "user_profile"

urlpatterns = [
    path("profile/", views.UserProfileDetailView.as_view(), name="profile_detail"),
    path("profile/update/", views.ProfileUpdateView.as_view(), name="profile_update"),
]

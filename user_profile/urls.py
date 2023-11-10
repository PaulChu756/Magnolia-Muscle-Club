from django.urls import path

from . import views
from user_profile import views as profile_views

app_name = "user_profile"

urlpatterns = [
    path("", views.UserProfileDetailView.as_view(), name="profile_detail"),
    path("update/", views.UserProfileUpdateView.as_view(), name="profile_update"),
]

from django.urls import path

from . import views

app_name = "user_profile"

urlpatterns = [
    path("userprofile/<int:pk>/", views.UserProfileDetailView.as_view(), name="userprofile-detail"),
    path("profile/update/", views.ProfileUpdateView.as_view(), name="profile_update"),
]

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('update_profile/', views.update_profile, name='update_profile'),
]
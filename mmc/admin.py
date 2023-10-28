from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'type_of_account', 'first_name', 'last_name']  # Adjust this as needed

admin.site.register(UserProfile, UserProfileAdmin)
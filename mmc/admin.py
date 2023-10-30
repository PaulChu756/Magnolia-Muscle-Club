from django.contrib import admin
from .models import UserProfile  # Import the UserProfile model
from .models import Day, Exercise, WorkoutSchedule
from .models import MealEntry
from .models import Notification

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['custom_user', 'type_of_account', 'first_name', 'last_name']  # Adjust this as needed
    actions = ['set_account_type_paid']

    def set_account_type_paid(modeladmin, request, queryset):
        # Assuming you want to set the selected users' account type to "Paid"
        queryset.update(type_of_account='Paid')
    set_account_type_paid.short_description = "Set selected users' account type to Paid"


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(WorkoutSchedule)
admin.site.register(Day)
admin.site.register(Exercise)
admin.site.register(MealEntry)
admin.site.register(Notification)

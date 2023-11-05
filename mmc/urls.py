from django.urls import path
from . import views
from mmc import views

app_name = "mmc"

urlpatterns = [
    # Other URL patterns...
    #path('update_profile/', views.update_profile, name='update_profile'),
    path('mmc/about', views.redirectTest, name='add')

     # URL pattern for a view that displays a list of Workout objects
    path('workouts/', views.WorkoutListView.as_view(), name='workout-list'),

    # URL pattern for a view that displays a user's profile
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),

    # URL patterns for other models and views
    path('weights/', views.WeightListView.as_view(), name='weight-list'),
    path('personal-bests/', views.PersonalBestListView.as_view(), name='personal-best-list'),
    path('workout-schedules/', views.WorkoutScheduleListView.as_view(), name='workout-schedule-list'),
    path('days/', views.DayListView.as_view(), name='day-list'),
    path('exercises/', views.ExerciseListView.as_view(), name='exercise-list'),
    path('workout-videos/', views.WorkOutVideosListView.as_view(), name='workout-videos-list'),
    path('food-library/', views.FoodLibraryListView.as_view(), name='food-library-list'),
    path('meal-entries/', views.MealEntryListView.as_view(), name='meal-entry-list'),
    path('notifications/', views.NotificationListView.as_view(), name='notification-list'),
]
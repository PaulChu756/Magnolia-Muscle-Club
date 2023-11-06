from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView

from .models import (
    Workout,
    Weight,
    PersonalBest,
    UserProfile,
    WorkoutSchedule,
    Day,
    Exercise,
    WorkOutVideos,
    FoodLibrary,
    MealEntry,
    Notification,
)

#May need extra_content field

# CreateView for the Workout model
class WorkoutCreateView(generic.CreateView):
    model = Workout
    fields = '__all__'
    success_url = reverse_lazy('mmc:workout-list')
    template_name = 'generic_workout_form.html'
    extra_context = {"title_text": "Add Workout", "button_text": "Add"}

# CreateView for the Weight model
class WeightCreateView(generic.CreateView):
    model = Weight
    fields = '__all__'
    success_url = reverse_lazy('mmc:weight-list')
    template_name = 'generic_weight_form.html'
    extra_context = {"title_text": "Add Weight", "button_text": "Add"}

# CreateView for the PersonalBest model
class PersonalBestCreateView(generic.CreateView):
    model = PersonalBest
    fields = '__all__'
    success_url = reverse_lazy('mmc:personalbest-list')
    template_name = 'generic_personalbest_form.html'
    extra_context = {"title_text": "Add Personal Best", "button_text": "Add"}

# CreateView for the UserProfile model
class UserProfileCreateView(generic.CreateView):
    model = UserProfile
    fields = '__all__'
    success_url = reverse_lazy('mmc:userprofile-list')
    template_name = 'generic_userprofile_form.html'
    extra_context = {"title_text": "Add User Profile", "button_text": "Add"}

# CreateView for the WorkoutSchedule model
class WorkoutScheduleCreateView(generic.CreateView):
    model = WorkoutSchedule
    fields = '__all__'
    success_url = reverse_lazy('mmc:workoutschedule-list')
    template_name = 'generic_workoutschedule_form.html'
    extra_context = {"title_text": "Add Workout Schedule", "button_text": "Add"}

# CreateView for the Day model
class DayCreateView(generic.CreateView):
    model = Day
    fields = '__all__'
    success_url = reverse_lazy('mmc:day-list')
    template_name = 'generic_day_form.html'
    extra_context = {"title_text": "Add Day", "button_text": "Add"}

# CreateView for the Exercise model
class ExerciseCreateView(generic.CreateView):
    model = Exercise
    fields = '__all__'
    success_url = reverse_lazy('mmc:exercise-list')
    template_name = 'generic_exercise_form.html'
    extra_context = {"title_text": "Add Exercise", "button_text": "Add"}

# CreateView for the WorkOutVideos model
class WorkOutVideosCreateView(generic.CreateView):
    model = WorkOutVideos
    fields = '__all__'
    success_url = reverse_lazy('mmc:workoutvideos-list')
    template_name = 'generic_workoutvideos_form.html'
    extra_context = {"title_text": "Add Workout Videos", "button_text": "Add"}

# CreateView for the FoodLibrary model
class FoodLibraryCreateView(generic.CreateView):
    model = FoodLibrary
    fields = '__all__'
    success_url = reverse_lazy('mmc:foodlibrary-list')
    template_name = 'generic_foodlibrary_form.html'
    extra_context = {"title_text": "Add Food Library", "button_text": "Add"}

# CreateView for the MealEntry model
class MealEntryCreateView(generic.CreateView):
    model = MealEntry
    fields = '__all__'
    success_url = reverse_lazy('mmc:mealentry-list')
    template_name = 'generic_mealentry_form.html'
    extra_context = {"title_text": "Add Meal Entry", "button_text": "Add"}

# CreateView for the Notification model
class NotificationCreateView(generic.CreateView):
    model = Notification
    fields = '__all__'
    success_url = reverse_lazy('mmc:notification-list')
    template_name = 'generic_notification_form.html'
    extra_context = {"title_text": "Add Notification", "button_text": "Add"}


# Refactored List Views with "generic" parameter
# ListView for Workout model
class WorkoutListView(generic.ListView):
    model = Workout
    template_name = 'workout_list.html'  # Create a template for the list view
    context_object_name = 'workouts'  # The variable name to access objects in the template

# ListView and DetailView for Weight model
class WeightListView(generic.ListView):
    model = Weight
    template_name = 'weight_list.html'
    context_object_name = 'weights'

# ListView and DetailView for PersonalBest model
class PersonalBestListView(generic.ListView):
    model = PersonalBest
    template_name = 'personalbest_list.html'
    context_object_name = 'personalbests'

# ListView and DetailView for UserProfile model
class UserProfileListView(generic.ListView):
    model = UserProfile
    template_name = 'userprofile_list.html'
    context_object_name = 'userprofiles'

# ListView and DetailView for WorkoutSchedule model
class WorkoutScheduleListView(generic.ListView):
    model = WorkoutSchedule
    template_name = 'workoutschedule_list.html'
    context_object_name = 'workoutschedules'

# ListView and DetailView for Day model
class DayListView(generic.ListView):
    model = Day
    template_name = 'day_list.html'
    context_object_name = 'days'

# ListView and DetailView for Exercise model
class ExerciseListView(generic.ListView):
    model = Exercise
    template_name = 'exercise_list.html'
    context_object_name = 'exercises'

# ListView and DetailView for WorkOutVideos model
class WorkOutVideosListView(generic.ListView):
    model = WorkOutVideos
    template_name = 'workoutvideos_list.html'
    context_object_name = 'workoutvideos'

# ListView and DetailView for FoodLibrary model
class FoodLibraryListView(generic.ListView):
    model = FoodLibrary
    template_name = 'foodlibrary_list.html'
    context_object_name = 'foodlibraries'

# ListView and DetailView for MealEntry model
class MealEntryListView(generic.ListView):
    model = MealEntry
    template_name = 'mealentry_list.html'
    context_object_name = 'mealentries'

# ListView and DetailView for Notification model
class NotificationListView(generic.ListView):
    model = Notification
    template_name = 'notification_list.html'
    context_object_name = 'notifications'



# DetailView for Workout model
class WorkoutDetailView(DetailView):
    model = Workout

class WeightDetailView(DetailView):
    model = Weight

class PersonalBestDetailView(DetailView):
    model = PersonalBest

class UserProfileDetailView(DetailView):
    model = UserProfile

class WorkoutScheduleDetailView(DetailView):
    model = WorkoutSchedule

class DayDetailView(DetailView):
    model = Day

class ExerciseDetailView(DetailView):
    model = Exercise

class WorkOutVideosDetailView(DetailView):
    model = WorkOutVideos

class FoodLibraryDetailView(DetailView):
    model = FoodLibrary

class MealEntryDetailView(DetailView):
    model = MealEntry

class NotificationDetailView(DetailView):
    model = Notification



# UpdateView for the Workout model
class WorkoutUpdateView(generic.UpdateView):
    model = Workout
    template_name = 'generic_workout_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mmc:workout-list')

# UpdateView for the Weight model
class WeightUpdateView(generic.UpdateView):
    model = Weight
    template_name = 'weight_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mmc:weight-list')

# UpdateView for the PersonalBest model
class PersonalBestUpdateView(generic.UpdateView):
    model = PersonalBest
    template_name = 'personalbest_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mmc:personalbest-list')

# UpdateView for the UserProfile model
class UserProfileUpdateView(generic.UpdateView):
    model = UserProfile
    template_name = 'userprofile_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mmc:userprofile-list')

# UpdateView for the WorkoutSchedule model
class WorkoutScheduleUpdateView(generic.UpdateView):
    model = WorkoutSchedule
    template_name = 'workoutschedule_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mmc:workoutschedule-list')

# UpdateView for the Day model
class DayUpdateView(generic.UpdateView):
    model = Day
    template_name = 'day_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mmc:day-list')

# UpdateView for the Exercise model
class ExerciseUpdateView(generic.UpdateView):
    model = Exercise
    template_name = 'exercise_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mmc:exercise-list')

# UpdateView for the WorkOutVideos model
class WorkOutVideosUpdateView(generic.UpdateView):
    model = WorkOutVideos
    template_name = 'workoutvideos_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mmc:workoutvideos-list')

# UpdateView for the FoodLibrary model
class FoodLibraryUpdateView(generic.UpdateView):
    model = FoodLibrary
    template_name = 'foodlibrary_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mmc:foodlibrary-list')

# UpdateView for the MealEntry model
class MealEntryUpdateView(generic.UpdateView):
    model = MealEntry
    template_name = 'mealentry_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mmc:mealentry-list')

# UpdateView for the Notification model
class NotificationUpdateView(generic.UpdateView):
    model = Notification
    template_name = 'notification_form.html'
    fields = '__all__'
    success_url = reverse_lazy('mmc:notification-list')



# DeleteView for the Workout model
class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = 'workout_confirm_delete.html'
    success_url = reverse_lazy('mmc:workout-list')

# DeleteView for the Weight model
class WeightDeleteView(DeleteView):
    model = Weight
    template_name = 'weight_confirm_delete.html'
    success_url = reverse_lazy('mmc:weight-list')

# DeleteView for the PersonalBest model
class PersonalBestDeleteView(DeleteView):
    model = PersonalBest
    template_name = 'personalbest_confirm_delete.html'
    success_url = reverse_lazy('mmc:personalbest-list')

# DeleteView for the UserProfile model
class UserProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = 'userprofile_confirm_delete.html'
    success_url = reverse_lazy('mmc:userprofile-list')

# DeleteView for the WorkoutSchedule model
class WorkoutScheduleDeleteView(DeleteView):
    model = WorkoutSchedule
    template_name = 'workoutschedule_confirm_delete.html'
    success_url = reverse_lazy('mmc:workoutschedule-list')

# DeleteView for the Day model
class DayDeleteView(DeleteView):
    model = Day
    template_name = 'day_confirm_delete.html'
    success_url = reverse_lazy('mmc:day-list')

# DeleteView for the Exercise model
class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = 'exercise_confirm_delete.html'
    success_url = reverse_lazy('mmc:exercise-list')

# DeleteView for the WorkOutVideos model
class WorkOutVideosDeleteView(DeleteView):
    model = WorkOutVideos
    template_name = 'workoutvideos_confirm_delete.html'
    success_url = reverse_lazy('mmc:workoutvideos-list')

# DeleteView for the FoodLibrary model
class FoodLibraryDeleteView(DeleteView):
    model = FoodLibrary
    template_name = 'foodlibrary_confirm_delete.html'
    success_url = reverse_lazy('mmc:foodlibrary-list')

# DeleteView for the MealEntry model
class MealEntryDeleteView(DeleteView):
    model = MealEntry
    template_name = 'mealentry_confirm_delete.html'
    success_url = reverse_lazy('mmc:mealentry-list')

# DeleteView for the Notification model
class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = 'notification_confirm_delete.html'
    success_url = reverse_lazy('mmc:notification-list')
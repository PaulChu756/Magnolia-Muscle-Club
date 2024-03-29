from django.urls import reverse_lazy
from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from user_profile.mixins import MemberRequiredMixin, TrainerRequiredMixin


# Create your views here.
# CreateView for the Workout model
class WorkoutCreateView(TrainerRequiredMixin, generic.CreateView):
    model = models.Workout
    fields = "__all__"
    success_url = reverse_lazy("workout:workout-list")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Add Workout", "button_text": "Add"}


# CreateView for the Weight model
class WeightCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Weight
    fields = "__all__"
    success_url = reverse_lazy("workout:weight-list")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Add Weight", "button_text": "Add"}


# CreateView for the PersonalBest model
class PersonalBestCreateView(MemberRequiredMixin, generic.CreateView):
    model = models.PersonalBest
    fields = "__all__"
    success_url = reverse_lazy("workout:personalbest-list")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Add Personal Best", "button_text": "Add"}


# CreateView for the WorkoutSchedule model
class WorkoutScheduleCreateView(TrainerRequiredMixin, generic.CreateView):
    model = models.WorkoutSchedule
    fields = "__all__"
    success_url = reverse_lazy("workout:workoutschedule-list")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Add Workout Schedule", "button_text": "Add"}


# CreateView for the Day model
class DayCreateView(TrainerRequiredMixin, generic.CreateView):
    model = models.Day
    fields = "__all__"
    success_url = reverse_lazy("workout:day-list")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Add Day", "button_text": "Add"}


# CreateView for the Exercise model
class ExerciseCreateView(TrainerRequiredMixin, generic.CreateView):
    model = models.Exercise
    fields = "__all__"
    success_url = reverse_lazy("workout:exercise-list")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Add Exercise", "button_text": "Add"}


# CreateView for the WorkOutVideos model
class WorkOutVideosCreateView(TrainerRequiredMixin, generic.CreateView):
    model = models.WorkOutVideos
    fields = "__all__"
    success_url = reverse_lazy("workout:workoutvideos-list")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Add Workout Videos", "button_text": "Add"}




# Refactored List Views with "generic" parameter
# ListView for Workout model
class WorkoutListView(generic.ListView):
    model = models.Workout
    template_name = "workout_list.html"  # Create a template for the list view
    context_object_name = "workouts"  # The variable name to access objects in the template


# ListView and DetailView for Weight model
class WeightListView(LoginRequiredMixin, generic.ListView):
    model = models.Weight
    template_name = "weight_list.html"
    context_object_name = "weights"


# ListView and DetailView for PersonalBest model
class PersonalBestListView(generic.ListView):
    model = models.PersonalBest
    template_name = "personalbest_list.html"
    context_object_name = "personalbests"


# ListView and DetailView for WorkoutSchedule model
class WorkoutScheduleListView(generic.ListView):
    model = models.WorkoutSchedule
    template_name = "workoutschedule_list.html"
    context_object_name = "workoutschedules"


# ListView and DetailView for Day model
class DayListView(generic.ListView):
    model = models.Day
    template_name = "day_list.html"
    context_object_name = "days"


# ListView and DetailView for Exercise model
class ExerciseListView(generic.ListView):
    model = models.Exercise
    template_name = "exercise_list.html"
    context_object_name = "exercises"


# ListView and DetailView for WorkOutVideos model
class WorkOutVideosListView(generic.ListView):
    model = models.WorkOutVideos
    template_name = "workoutvideos_list.html"
    context_object_name = "workoutvideos"




class WorkoutDetailView(generic.DetailView):
    model = models.Workout


class WeightDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Weight


class PersonalBestDetailView(generic.DetailView):
    model = models.PersonalBest


class WorkoutScheduleDetailView(generic.DetailView):
    model = models.WorkoutSchedule


class DayDetailView(generic.DetailView):
    model = models.Day


class ExerciseDetailView(generic.DetailView):
    model = models.Exercise


class WorkOutVideosDetailView(generic.DetailView):
    model = models.WorkOutVideos




class WorkoutUpdateView(TrainerRequiredMixin, generic.UpdateView):
    model = models.Workout
    fields = "__all__"
    success_url = reverse_lazy("workout:workout-list")
    template_name = "generic_workout_form.html"
    extra_context = {"title_text": "Edit Workout", "button_text": "Update"}

# UpdateView for the Weight model
class WeightUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Weight
    fields = "__all__"
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("workout:weight-list")
    extra_context = {"title_text": "Edit Weight", "button_text": "Update"}


# UpdateView for the WorkoutSchedule model
class WorkoutScheduleUpdateView(TrainerRequiredMixin, generic.UpdateView):
    model = models.WorkoutSchedule
    fields = "__all__"
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("workout:workoutschedule-list")
    extra_context = {"title_text": "Edit Workout Schedule", "button_text": "Update"}

# UpdateView for the PersonalBest model
class PersonalBestUpdateView(MemberRequiredMixin, generic.UpdateView):
    model = models.PersonalBest
    fields = "__all__"
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("workout:personalbest-list")
    extra_context = {"title_text": "Edit Personal Best", "button_text": "Update"}

# UpdateView for the Day model
class DayUpdateView(TrainerRequiredMixin, generic.UpdateView):
    model = models.Day
    fields = "__all__"
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("workout:day-list")
    extra_context = {"title_text": "Edit Day", "button_text": "Update"}


# UpdateView for the Exercise model
class ExerciseUpdateView(TrainerRequiredMixin, generic.UpdateView):
    model = models.Exercise
    fields = "__all__"
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("workout:exercise-list")
    extra_context = {"title_text": "Edit Exercise", "button_text": "Update"}


# UpdateView for the WorkOutVideos model
class WorkOutVideosUpdateView(TrainerRequiredMixin, generic.UpdateView):
    model = models.WorkOutVideos
    fields = "__all__"
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("workout:workoutvideos-list")
    extra_context = {"title_text": "Edit Workout Videos", "button_text": "Update"}





# DeleteView for the Workout model
class WorkoutDeleteView(TrainerRequiredMixin, generic.DeleteView):
    model = models.Workout
    success_url = reverse_lazy("workout:workout-list")
    template_name = "generic_confirm_delete.html"
    extra_content = {"title_text": "Delete Workout"}


# DeleteView for the Weight model
class WeightDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Weight
    success_url = reverse_lazy("workout:weight-list")
    template_name = "generic_confirm_delete.html"
    extra_content = {"title_text": "Delete Weight"}


# DeleteView for the PersonalBest model
class PersonalBestDeleteView(MemberRequiredMixin, generic.DeleteView):
    model = models.PersonalBest
    success_url = reverse_lazy("workout:personalbest-list")
    template_name = "generic_confirm_delete.html"
    extra_content = {"title_text": "Delete Personal Best"}

# DeleteView for the WorkoutSchedule model
class WorkoutScheduleDeleteView(TrainerRequiredMixin, generic.DeleteView):
    model = models.WorkoutSchedule
    success_url = reverse_lazy("workout:workoutschedule-list")
    template_name = "generic_confirm_delete.html"
    extra_content = {"title_text": "Delete Workout Schedule"}

# DeleteView for the Day model
class DayDeleteView(TrainerRequiredMixin, generic.DeleteView):
    model = models.Day
    success_url = reverse_lazy("workout:day-list")
    template_name = "generic_confirm_delete.html"
    extra_content = {"title_text": "Delete Day"}

# DeleteView for the Exercise model
class ExerciseDeleteView(TrainerRequiredMixin, generic.DeleteView):
    model = models.Exercise
    success_url = reverse_lazy("workout:exercise-list")
    template_name = "generic_confirm_delete.html"
    extra_content = {"title_text": "Delete Exercise"}

# DeleteView for the WorkOutVideos model
class WorkOutVideosDeleteView(TrainerRequiredMixin, generic.DeleteView):
    model = models.WorkOutVideos
    success_url = reverse_lazy("workout:workoutvideos-list")
    template_name = "generic_confirm_delete.html"
    extra_content = {"title_text": "Delete Workout Videos"}

from django.urls import reverse_lazy
from django.views import generic
from user_profile.mixins import MemberRequiredMixin, TrainerRequiredMixin

from . import models


class FoodLibraryCreateView(TrainerRequiredMixin, generic.CreateView):
    model = models.FoodLibrary
    fields = "__all__"
    success_url = reverse_lazy("meal:foodlibrary-list")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Add Food Library", "button_text": "Add"}


# CreateView for the MealEntry model
class MealEntryCreateView(TrainerRequiredMixin, generic.CreateView):
    model = models.MealEntry
    fields = "__all__"
    success_url = reverse_lazy("meal:mealentry-list")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Add Meal Entry", "button_text": "Add"}


# ListView and DetailView for FoodLibrary model
class FoodLibraryListView(generic.ListView):
    model = models.FoodLibrary
    template_name = "foodlibrary_list.html"
    context_object_name = "foodlibraries"


# ListView and DetailView for MealEntry model
class MealEntryListView(generic.ListView):
    model = models.MealEntry
    template_name = "mealentry_list.html"
    context_object_name = "mealentries"


class FoodLibraryDetailView(generic.DetailView):
    model = models.FoodLibrary


class MealEntryDetailView(generic.DetailView):
    model = models.MealEntry


# UpdateView for the FoodLibrary model
class FoodLibraryUpdateView(TrainerRequiredMixin, generic.UpdateView):
    model = models.FoodLibrary
    fields = "__all__"
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("meal:foodlibrary-list")
    extra_context = {"title_text": "Edit Food Library", "button_text": "Update"}


# UpdateView for the MealEntry model
class MealEntryUpdateView(TrainerRequiredMixin, generic.UpdateView):
    model = models.MealEntry
    fields = "__all__"
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("meal:mealentry-list")
    extra_context = {"title_text": "Edit Meal Entry", "button_text": "Update"}


# DeleteView for the FoodLibrary model
class FoodLibraryDeleteView(TrainerRequiredMixin, generic.DeleteView):
    model = models.FoodLibrary
    success_url = reverse_lazy("meal:foodlibrary-list")
    template_name = "generic_confirm_delete.html"
    extra_content = {"title_text": "Delete Food Library"}


# DeleteView for the MealEntry model
class MealEntryDeleteView(TrainerRequiredMixin, generic.DeleteView):
    model = models.MealEntry
    success_url = reverse_lazy("meal:mealentry-list")
    template_name = "generic_confirm_delete.html"
    extra_content = {"title_text": "Delete Meal Entry"}

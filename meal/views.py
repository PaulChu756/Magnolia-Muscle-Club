from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from user_profile.mixins import MemberRequiredMixin, TrainerRequiredMixin

from . import models, mixins


class FoodLibraryCreateView(TrainerRequiredMixin, generic.CreateView):
    model = models.FoodLibrary
    fields = "__all__"
    success_url = reverse_lazy("meal:foodlibrary-list")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Add Food Library", "button_text": "Add"}


# CreateView for the MealEntry model
class MealEntryCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.MealEntry
    fields = ["meal_type", "food_item", "calories_consumed"]
    success_url = reverse_lazy("meal:mealentry-list")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Add Meal Entry", "button_text": "Add"}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# ListView and DetailView for FoodLibrary model
class FoodLibraryListView(generic.ListView):
    model = models.FoodLibrary
    template_name = "foodlibrary_list.html"
    context_object_name = "foodlibraries"


# ListView and DetailView for MealEntry model
class MealEntryListView(LoginRequiredMixin, generic.ListView):
    model = models.MealEntry
    template_name = "mealentry_list.html"
    context_object_name = "mealentries"

    def get_queryset(self):
        # Ensure the user is logged in before trying to fetch their meal entries
        return models.MealEntry.objects.filter(user=self.request.user)


class FoodLibraryDetailView(generic.DetailView):
    model = models.FoodLibrary


class MealEntryDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.MealEntry
    template_name = "mealentry_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            raise Http404("You do not have permission to access this page.")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


# UpdateView for the FoodLibrary model
class FoodLibraryUpdateView(TrainerRequiredMixin, generic.UpdateView):
    model = models.FoodLibrary
    fields = "__all__"
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("meal:foodlibrary-list")
    extra_context = {"title_text": "Edit Food Library", "button_text": "Update"}


# UpdateView for the MealEntry model
class MealEntryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.MealEntry
    fields = ["meal_type", "food_item", "calories_consumed"]
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("meal:mealentry-list")
    extra_context = {"title_text": "Edit Meal Entry", "button_text": "Update"}

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("You do not have permission to access this page.")
        return obj


# DeleteView for the FoodLibrary model
class FoodLibraryDeleteView(TrainerRequiredMixin, generic.DeleteView):
    model = models.FoodLibrary
    success_url = reverse_lazy("meal:foodlibrary-list")
    template_name = "generic_confirm_delete.html"
    extra_content = {"title_text": "Delete Food Library"}


# DeleteView for the MealEntry model
class MealEntryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.MealEntry
    success_url = reverse_lazy("meal:mealentry-list")
    template_name = "generic_confirm_delete.html"
    extra_content = {"title_text": "Delete Meal Entry"}

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("You do not have permission to access this page.")
        return obj

from django.urls import path

from . import views

app_name = 'meal'

urlpatterns = [
    # Create views
    path("foodlibrary/create/", views.FoodLibraryCreateView.as_view(), name="foodlibrary-create"),
    path("mealentry/create/", views.MealEntryCreateView.as_view(), name="mealentry-create"),

    # List views
    path("foodlibrary/list/", views.FoodLibraryListView.as_view(), name="foodlibrary-list"),
    path("mealentry/list/", views.MealEntryListView.as_view(), name="mealentry-list"),
    path("foodlibrary/<int:pk>/", views.FoodLibraryDetailView.as_view(), name="foodlibrary-detail"),
    path("mealentry/<int:pk>/", views.MealEntryDetailView.as_view(), name="mealentry-detail"),

    # UpdateView URL patterns
    path("foodlibrary/<int:pk>/update/", views.FoodLibraryUpdateView.as_view(), name="foodlibrary-update",),
    path("mealentry/<int:pk>/update/", views.MealEntryUpdateView.as_view(), name="mealentry-update"),

    # DeleteView URL patterns
    path("foodlibrary/<int:pk>/delete/", views.FoodLibraryDeleteView.as_view(), name="foodlibrary-delete",),
    path("mealentry/<int:pk>/delete/", views.MealEntryDeleteView.as_view(), name="mealentry-delete"),
]

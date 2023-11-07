from django.urls import path

from . import views

app_name = "workout"

urlpatterns = [
    # Create views
    path("workout/create/", views.WorkoutCreateView.as_view(), name="workout-create"),
    path("weight/create/", views.WeightCreateView.as_view(), name="weight-create"),
    path("personalbest/create/", views.PersonalBestCreateView.as_view(), name="personalbest-create"),
    path("workoutschedule/create/", views.WorkoutScheduleCreateView.as_view(), name="workoutschedule-create",),
    path("day/create/", views.DayCreateView.as_view(), name="day-create"),
    path("exercise/create/", views.ExerciseCreateView.as_view(), name="exercise-create"),
    path("workoutvideos/create/", views.WorkOutVideosCreateView.as_view(), name="workoutvideos-create",),


    # List views
    path("workout/list/", views.WorkoutListView.as_view(), name="workout-list"),
    path("weight/list/", views.WeightListView.as_view(), name="weight-list"),
    path("personalbest/list/", views.PersonalBestListView.as_view(), name="personalbest-list"),
    path("workoutschedule/list/", views.WorkoutScheduleListView.as_view(), name="workoutschedule-list",),
    path("day/list/", views.DayListView.as_view(), name="day-list"),
    path("exercise/list/", views.ExerciseListView.as_view(), name="exercise-list"),
    path("workoutvideos/list/", views.WorkOutVideosListView.as_view(), name="workoutvideos-list",),


    # Detail views
    path("workout/<int:pk>/", views.WorkoutDetailView.as_view(), name="workout-detail"),
    path("weight/<int:pk>/", views.WeightDetailView.as_view(), name="weight-detail"),
    path("personalbest/<int:pk>/", views.PersonalBestDetailView.as_view(), name="personalbest-detail"),
    path("workoutschedule/<int:pk>/", views.WorkoutScheduleDetailView.as_view(), name="workoutschedule-detail",),
    path("day/<int:pk>/", views.DayDetailView.as_view(), name="day-detail"),
    path("exercise/<int:pk>/", views.ExerciseDetailView.as_view(), name="exercise-detail"),
    path("workoutvideos/<int:pk>/", views.WorkOutVideosDetailView.as_view(), name="workoutvideos-detail",),

    #Updates
    path("workout/<int:pk>/update/", views.WorkoutUpdateView.as_view(), name="workout-update"),
    path("weight/<int:pk>/update/", views.WeightUpdateView.as_view(), name="weight-update"),
    path("personalbest/<int:pk>/update/", views.PersonalBestUpdateView.as_view(), name="personalbest-update",),
    path("workoutschedule/<int:pk>/update/", views.WorkoutScheduleUpdateView.as_view(), name="workoutschedule-update",),
    path("day/<int:pk>/update/", views.DayUpdateView.as_view(), name="day-update"),
    path("exercise/<int:pk>/update/", views.ExerciseUpdateView.as_view(), name="exercise-update"),
    path("workoutvideos/<int:pk>/update/", views.WorkOutVideosUpdateView.as_view(), name="workoutvideos-update",),


    #Delete
    path("workout/<int:pk>/delete/", views.WorkoutDeleteView.as_view(), name="workout-delete"),
    path("weight/<int:pk>/delete/", views.WeightDeleteView.as_view(), name="weight-delete"),
    path("personalbest/<int:pk>/delete/", views.PersonalBestDeleteView.as_view(), name="personalbest-delete",),
    path("workoutschedule/<int:pk>/delete/", views.WorkoutScheduleDeleteView.as_view(), name="workoutschedule-delete",),
    path("day/<int:pk>/delete/", views.DayDeleteView.as_view(), name="day-delete"),
    path("exercise/<int:pk>/delete/", views.ExerciseDeleteView.as_view(), name="exercise-delete"),
    path("workoutvideos/<int:pk>/delete/", views.WorkOutVideosDeleteView.as_view(), name="workoutvideos-delete",),
]

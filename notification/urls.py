from django.urls import path

from . import views

app_name = "notification"

urlpatterns = [
    path(
        "notification/create/", views.NotificationCreateView.as_view(), name="notification-create"
    ),
    path("notification/list/", views.NotificationListView.as_view(), name="notification-list"),
    path(
        "notification/<int:pk>/", views.NotificationDetailView.as_view(), name="notification-detail"
    ),
    path(
        "notification/<int:pk>/update/",
        views.NotificationUpdateView.as_view(),
        name="notification-update",
    ),
    path(
        "notification/<int:pk>/delete/",
        views.NotificationDeleteView.as_view(),
        name="notification-delete",
    ),
]

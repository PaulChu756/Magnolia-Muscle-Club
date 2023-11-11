from django.urls import path

from . import views

app_name = "notification"

urlpatterns = [
    path("create/", views.NotificationCreateView.as_view(), name="notification-create"),
    path("list/", views.NotificationListView.as_view(), name="notification-list"),
    path("<int:pk>/", views.NotificationDetailView.as_view(), name="notification-detail"),
    path("<int:pk>/update/", views.NotificationUpdateView.as_view(), name="notification-update",),
    path("<int:pk>/delete/", views.NotificationDeleteView.as_view(), name="notification-delete",),
]

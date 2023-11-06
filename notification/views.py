from django.urls import reverse_lazy
from django.views import generic

from . import models


# CreateView for the Notification model
class NotificationCreateView(generic.CreateView):
    model = models.Notification
    fields = "__all__"
    success_url = reverse_lazy("notification:notification-list")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Add Notification", "button_text": "Add"}


# ListView and DetailView for Notification model
class NotificationListView(generic.ListView):
    model = models.Notification
    template_name = "notifcation_list.html"
    context_object_name = "notifications"


# UpdateView for the Notification model
class NotificationUpdateView(generic.UpdateView):
    model = models.Notification
    fields = "__all__"
    template_name = "notification_form.html"
    success_url = reverse_lazy("notification:notification-list")
    extra_context = {"title_text": "Edit Notification", "button_text": "Update"}


class NotificationDetailView(generic.DetailView):
    model = models.Notification


# DeleteView for the Notification model
class NotificationDeleteView(generic.DeleteView):
    model = models.Notification
    success_url = reverse_lazy("notification:notification-list")
    template_name = "notification_confirm_delete.html"
    extra_content = {"title_text": "Delete Notification"}

# mixins.py
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy

class UserPermissionMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("You do not have permission to access this page.")
        return obj
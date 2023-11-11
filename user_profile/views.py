from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from users.forms import CustomUserChangeForm
from users.models import CustomUser
from . import models

"""User profile view."""
from user_profile.forms import UserProfileUpdateForm
from user_profile.models import UserProfile

#polls app
class UserProfileDetailView(LoginRequiredMixin, DetailView):
    """Profile detail view.

    Reason why `slug_field` and `slug_url_kwargs` are set as `None`:
    - By default, in a `DetailView`, the object of the model is retrieved from the URL parameters.
    - In this case, as the model is `UserProfile`, the object of user is retrieved from the request.

    """

    model = UserProfile
    template_name = "user_profile/userprofile_detail.html"
    slug_field = None
    slug_url_kwarg = ""

    def get_object(self, queryset: list = None):
        """Owner of the object should be the current user."""
        return self.model.objects.filter(custom_user=self.request.user).first()


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Profile update view."""

    model = UserProfile
    form_class = UserProfileUpdateForm
    #fields=[""]
    success_url = reverse_lazy("user_profile:profile_detail")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Edit Profile", "button_text": "Update"}

    def get_object(self, queryset: list = None):
        """Get the `UserProfile` object the current logged in user."""
        return self.model.objects.filter(custom_user=self.request.user).first()

    # def get_context_data(self, **kwargs):
    #     """Add additional fields to the form.

    #     In addition to the age, gender, and picture fields of `UserProfile` object,
    #     add `first_name` and `last_name` fields of the `CustomUser` to the form.

    #     As `is_student` and `is_teacher` are boolean fields and mutually exclusive,
    #     combine them into a choice field `account_type`.

    #     Hence, to the `form` to be rendered by Django template, add three fields:
    #     `fist_name`, `last_name`, and `account_type`.

    #     """
    #     context = super().get_context_data(**kwargs)
    #     #account_type = 1 if self.request.user.userprofile.is_student else 2
    #     context["form"] = UserProfileUpdateForm(
    #         instance=self.request.user.userprofile,
    #         initial={
    #             "first_name": self.request.user.first_name,
    #             "last_name": self.request.user.last_name,
    #             #"account_type": account_type,
    #         },
    #     )
    #     return context

    def form_valid(self, form: object):
        """Set custom_user Field of the current object as the current user.

        - Update the `first_name` and `last_name` fields of the `CustomUser` model.
        - Set the `custom_user` (ForeignKey) field of `UserProfile` object of current user.
        - Update `is_student` and `is_teacher`: they are mutually exclusive.
        - Save the changes made to objects of `user_profile` and `custom_user` objects to the DB.

        """
        user_profile = form.save(commit=False)
        custom_user = self.request.user
        user_profile.custom_user = custom_user

        custom_user.first_name = form.cleaned_data["first_name"]
        custom_user.last_name = form.cleaned_data["last_name"]
        #account_type = int(form.cleaned_data["account_type"])

        # if account_type == 1:
        #     user_profile.is_student, user_profile.is_teacher = True, False
        # else:
        #     user_profile.is_student, user_profile.is_teacher = False, True

        if self.request.user.userprofile.is_free_account:
            return 'free'
        elif self.request.user.userprofile.is_paid_account:
            return 'paid'
        elif self.request.user.userprofile.is_trainer_account:
            return 'trainer'
        else:
            return 'free'  # Default to free account

        user_profile.save()
        custom_user.save()
        return super().form_valid(form)



# class UserProfileDetailView(generic.DetailView):
#     model = models.UserProfile


# class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
#     """Profile update view."""

#     model = CustomUser
#     form_class = CustomUserChangeForm
#     template_name = "registration/profile_update.html"
#     success_url = reverse_lazy("users:profile_detail")

#     def form_valid(self, form):
#         form.instance.modified_by = self.request.user
#         userprofile = models.UserProfile.objects.get_or_create(
#             first_name=form.cleaned_data["first_name"],
#             last_name=form.cleaned_data["last_name"],
#             picture=form.cleaned_data["picture"],
#             weight=form.cleaned_data["weight"],
#             height=form.cleaned_data["height"],
#             phone=form.cleaned_data["phone"],
#             gender=form.cleaned_data["gender"],
#         )
#         userprofile.save()
#         return super().form_valid(form)

#     def get_object(self, queryset=None):
#         """Owner of the object should be the current user."""
#         return self.request.user

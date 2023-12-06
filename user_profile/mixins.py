"""User role Mixins."""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class UserProfileRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """User Profile Object Required Mixin."""

    def test_func(self) -> bool:
        """Overriding `test_func` to check if the current logged in user is student.

        Returns
        -------
        bool
            True, when there is a `UserProfile` object for the current user.
            False, otherwise.

        """
        userprofile = self.request.user.userprofile
        return userprofile.is_free_account or userprofile.is_trainer_account or userprofile.is_paid_account

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
        return redirect("user_profile:profile_update")



class MemberRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Member role required mixin."""

    def test_func(self) -> bool:
        """Overriding `test_func` to check if the current logged in user is Member.

        Returns:
        -------
        bool
            True, when current user is Member.
            False, otherwise.

        """
        return self.request.user.userprofile.is_free_account

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
        redirect_url = reverse_lazy("workout:workout-list")
        return redirect(redirect_url)


class TrainerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Teacher role required mixin."""

    def test_func(self) -> bool:
        """Overriding `test_func` to check if the current logged in user is teacher.

        Returns:
        -------
        bool
            True, when current user is member.
            False, otherwise.

        """
        return self.request.user.userprofile.is_trainer_account

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
        redirect_url = reverse_lazy("workout:workout-list")
        return redirect(redirect_url)

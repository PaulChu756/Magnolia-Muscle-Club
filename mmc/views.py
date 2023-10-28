from django.shortcuts import render, redirect
from .forms import UserProfileForm

def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page after updating
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'update_user_profile.html', {'form': form})

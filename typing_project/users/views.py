from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # cleaned_data is a dictionary
            username = form.cleaned_data.get('username')
            # Flash message, 1 time alert
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Add decorator, adds functionality to an existing function
@login_required
def profile(request):
    if request.method == 'POST':
        # Pass post data to forms
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        # Provide file data (image) that user provides as well
        profile_update_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            # Implement POST-GET Redirect pattern
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }
    return render(request, 'users/profile.html', context)

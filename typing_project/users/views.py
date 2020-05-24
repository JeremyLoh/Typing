from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


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
    return render(request, 'users/profile.html')

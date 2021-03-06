from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # Required field setting is true by default
    email = forms.EmailField()

    # Nested namespace for configurations
    # Keep configurations in one place
    class Meta:
        # Specify model that form should interact with (e.g. during save())
        model = User
        # Fields to be shown in form (in order)
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # Form used to update User model
    # ModelForm, to work with specific database model
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']

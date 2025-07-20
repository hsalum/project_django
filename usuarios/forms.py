from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar 

class registerForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


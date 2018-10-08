from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)

class UserUpdateForm(forms.ModelForm): #ModelForm allows us to create a form that would work with specefic database models
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'portfolio', 'image',)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, CustomUserManager

class SignInForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")
    
    class Meta:
        model = CustomUser
        fields = ("email", "nickname", "password1", "password2", )
        
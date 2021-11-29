'''
Forms for user application
'''
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class UserSignUpForm(UserCreationForm):
    """User sign-up form implementation"""

    email = forms.EmailField(help_text="Write a valid email address.")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]
    

class SignInForm(AuthenticationForm):
    pass
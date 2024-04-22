from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username" , "email" , "password1" , "password2")
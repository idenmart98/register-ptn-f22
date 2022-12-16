from django import forms
from .models import User


class UserLoginRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        
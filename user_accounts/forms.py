from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user_accounts.models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    user_type = forms.ChoiceField(choices=Profile.USER_TYPE_CHOICE)
    date_of_birth = forms.DateField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'date_of_birth', 'password1', 'password2']

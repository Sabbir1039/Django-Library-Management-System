from django import forms
from .models import Author, Book

from django.contrib.auth.models import User  # Django builtin User model
from django.contrib.auth.forms import UserCreationForm  # Django builtin user form


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

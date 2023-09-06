from django.shortcuts import render, redirect
from django.contrib import messages
from user_accounts.forms import UserRegistrationForm
from user_accounts.models import Profile

# Create your views here.

def register(request):
    if request.method == 'POST':
        forms = UserRegistrationForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            Profile.objects.create(
                user = user,
                user_type = forms.cleaned_data['user_type'],
                date_of_birth = forms.cleaned_data['date_of_birth']
            )
            username = forms.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}!')
            return redirect('login')
        else:
            messages.error(request, f'Something went wrong!')
            
    forms = UserRegistrationForm()
    context = {
        'title': 'Sign Up',
        'forms': forms,
    }
    return render(request, 'user_accounts/register.html', context)
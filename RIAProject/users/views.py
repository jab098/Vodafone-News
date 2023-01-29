from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# register user


def register(request):
    if request.method == 'POST':
        # this happens after the user submits the sign up form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            # using flash message
            messages.success(request, f'Account created for {username}')
            # redirect user to the home screen now they have created an account
            return redirect('home')
    else:
        form = UserCreationForm()
        
    return render(request=request, template_name='users/register.html', context={'form': form})

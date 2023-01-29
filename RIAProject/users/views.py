from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

from .forms import UserRegisterForm

def register(request):
    # register user
    if request.method == 'POST':
        # this happens after the user submits the sign up form
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # save responses
            user = form.save()
            username = form.cleaned_data.get('username')
            # using flash message
            messages.success(request, f'Account created for {username}')
            # This allows users to view all posts, but they will not be able to write any posts unless they request access an are added to the 'Writers' group
            group = Group.objects.get(name='Viewers')
            user.groups.add(group)
            # redirect user to the home screen now they have created an account
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request=request, template_name='users/register.html', context={'form': form})

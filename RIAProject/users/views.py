from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.http import HttpRequest
from django.views.generic.base import TemplateView

from .forms import UserRegisterForm, WriterRequestForm

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
        # load the form when they first visit the page
        form = UserRegisterForm()

    return render(request=request, template_name='users/register.html', context={'form': form})

def requestWriterPermissions(request):
    if request.method == 'POST':
        # this happens after the user submits the form
        form = WriterRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Request submitted')
            # redirect user to the home screen now they have created an account
            return redirect('home')
            
    else:
        # load the form when they first visit the page
        current_user = request.user
        form = WriterRequestForm(initial={'requestee':current_user})

    return render(request=request, template_name='users/request_write.html', context={'form': form})

class SignedOutView(TemplateView):

    template_name = "registration/logged_out.html"

    def get(self, request: HttpRequest):
        logout(request)
        return render(request, self.template_name)
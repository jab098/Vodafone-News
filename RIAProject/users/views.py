from django.contrib import messages
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .forms import UserRegisterForm, WriterRequestForm, EditProfileForm 

class UserEditView(generic.UpdateView):
    #form_class = EditProfileForm
    template_name = 'users/my_account.html'
    success_url = reverse_lazy('home')
    fields = ['first_name', 'last_name', 'username', 'email']

    def get_object(self):
        return self.request.user

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
        requestee = request.user
        if form.is_valid():
            form.save(requestee)
            messages.success(request, f'Request submitted')
            # redirect user to the home screen now they have created an account
            return redirect('home')
            
    else:
        # load the form when they first visit the page
        current_user = request.user
        form = WriterRequestForm(initial={'requestee':current_user})

    return render(request=request, template_name='users/request_write.html', context={'form': form})
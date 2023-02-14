from django import forms
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import WriteRequest

class UserRegisterForm(UserCreationForm):
    # create a form that inherits from the standard usercreationform, so we can save extra fields including email address,first name and last name
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        # affecting the user model
        model = User
        # specifies the fields that will appear in the form, and the order in which they'll appear
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', ]


class WriterRequestForm(forms.ModelForm):
    """
    A form used to request writer permissions
    """
    class Meta:
        model = WriteRequest
        # this defines the fields that will be in the form
        fields = ("requestee","department","description")
        # this means the requestee isn't shown in the form, as it will be set to whoever is submitting the request
        exclude = ("requestee",)

    def save(request, requestee):
        department=request.cleaned_data['department']
        description=request.cleaned_data['description']
        request = WriteRequest.objects.create(requestee=requestee, department=department, description=description)
        return redirect('home')
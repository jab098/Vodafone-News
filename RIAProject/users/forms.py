from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

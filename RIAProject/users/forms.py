from django import forms
from django.contrib import messages
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
    # TODO: make the requestee field readonly
    # def __init__(self, *args, **kwargs):
    #     super(WriterRequestForm, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance:
    #         self.fields['requestee'].widget.attrs['readonly'] = True

    class Meta:
        # TODO: may have to create a new model for the request
        model = WriteRequest
        fields = ("requestee","department","description")

    def save(request):
        # TODO: creatre write request table
        print(request.cleaned_data)
        # TODO: ensure status is set to 0
        requestee=request.cleaned_data['requestee']
        department=request.cleaned_data['department']
        description=request.cleaned_data['description']
        request = WriteRequest.objects.create(requestee=requestee, department=department, description=description)
        # user.set_password(self.cleaned_data["password1"])
        # if commit:
        #     user.save()

    # def clean_requestee(self):
    #     if self.instance: 
    #         return self.instance.requestee
    #     else: 
    #         return self.fields['requestee']
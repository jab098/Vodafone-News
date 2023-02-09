from django.contrib import messages
from django.shortcuts import render

from .forms import WriterRequestForm

def requestWriterPermissions(request):
    if request.method == 'POST':
        # this happens after the user submits the form
        form = WriterRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Request submitted')
            # redirect user to the home screen now they have created an account
            # return redirect('home')
            
    else:
        # load the form when they first visit the page
        current_user = request.user
        form = WriterRequestForm(initial={'requestee':current_user})

    return render(request=request, template_name='users/request_write.html', context={'form': form})

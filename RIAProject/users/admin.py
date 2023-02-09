from django.contrib import admin
from django.contrib.auth.models import Group

from .models import WriteRequest

#this displays the admin panel with more detail
class WriteRequestAdmin(admin.ModelAdmin):
    
    #displays all properties from Post tuple for each post
    list_display = ('id', 'requestee', 'created_on', 'department', 'description', 'status')
    
    #the list_filter method filters the posts based on their status (submitted, accepted or rejected)
    list_filter = ("status",)
    
    #these are the attributes that will be used to allow articles to be searched for (i.e. can search by title or content)
    search_fields = ['id', 'requestee']

    def save_model(self, request, obj, form, change):
        # check if status has been set to submitted
        if form.cleaned_data['status'] == 1:
            # if so, update user permission before saving
            requestee = form.cleaned_data['requestee']
            group = Group.objects.get(name='Writers')
            requestee.groups.add(group)

        #regardless of the status, always save the form 
        super().save_model(request, obj, form, change)

admin.site.register(WriteRequest, WriteRequestAdmin)
from django.contrib import admin
from .models import WriteRequest

#this displays the admin panel with more detail
class WriteRequestAdmin(admin.ModelAdmin):
    
    #displays all properties from Post tuple for each post
    list_display = ('id', 'requestee', 'created_on', 'department', 'description', 'status')
    
    #the list_filter method filters the posts based on their status (submitted, accepted or rejected)
    list_filter = ("status",)
    
    #these are the attributes that will be used to allow articles to be searched for (i.e. can search by title or content)
    search_fields = ['id', 'requestee']

admin.site.register(WriteRequest, WriteRequestAdmin)
from django.contrib import admin
from .models import Post

#this displays the admin panel with more detail
class PostAdmin(admin.ModelAdmin):
    
    #displays all properties from Post tuple for each post
    list_display = ('title', 'slug', 'status','created_on')
    
    #the list_filter method filters theposts based on their status (published or draft)
    list_filter = ("status",)
    
    #these are the attributes that will be used to allow articles to be searched for (i.e. can search by title or content)
    search_fields = ['title', 'content']
    
    #automatically creates the slug based upon the title
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
from django import template
from django.contrib.auth.models import Group 

register = template.Library()

# creating custom template tag to check wheter a user is part of a specified group within the html files
@register.filter(name='in_group')
def in_group(user, group_name): 
    return user.groups.filter(name=group_name).exists() 

@register.filter(name='not_in_group')
def not_in_group(user, group_name): 
    return not user.groups.filter(name=group_name).exists() 
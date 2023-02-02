from django.views import generic
# requires users to login before they can view 
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

# displays the objects in the model 'Post' in a list in the given template

class PostList(LoginRequiredMixin, generic.ListView):
    login_url = '/users/accounts/login/'
    # Filtering the posts to only display published posts (in the tuple 1=publish) it
    # is also filtering the created on date to show the most recent post at the top
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

# DetailView gives a detailed view of a given object in the model at the specified template

class PostDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/users/accounts/login/'
    model = Post
    template_name = 'post_detail.html'

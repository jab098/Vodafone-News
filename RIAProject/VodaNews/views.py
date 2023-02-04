from django.views import generic
# requires users to login before they can view 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# easily converts titles into slugs by adding dashes and removing captial letters
from django.template.defaultfilters import slugify

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

class PostCreate(LoginRequiredMixin, generic.CreateView):
    login_url = '/users/accounts/login/'
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']   
    # TODO: add in slug
    def form_valid(self,form):
        # before getting the form ,set the author equal to the user currently logged in
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

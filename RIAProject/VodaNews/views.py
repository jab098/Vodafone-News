from django.views import generic
# requires users to login before they can view 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# easily converts titles into slugs by adding dashes and removing captial letters
from django.template.defaultfilters import slugify

from .models import Post, BlogComment
from .forms import CommentForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

# displays the objects in the model 'Post' in a list in the given template

def search_posts(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        searched_articles= Post.objects.filter(title__contains=searched)
        return render(request, 
            'search_posts.html',
            {'searched':searched,
            'searched_articles':searched_articles})
    else:
        return render(request, 
            'search_posts.html',
            {})

#function to get the id of the post and check whether the user has liked it or not in order to update the table
def LikeView(request, slug):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    #post = Post.objects.get(id=pk)
    liked = False
    #if user has already like the post
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(slug)]))
    
class PostList(LoginRequiredMixin, generic.ListView):
    login_url = '/users/accounts/login/'
    # Filtering the posts to only display published posts (in the tuple 1=publish) it
    # is also filtering the created on date to show the most recent post at the top
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class MyPostList(LoginRequiredMixin, generic.ListView):
    login_url = '/users/accounts/login/'
    # Filtering the posts to only display published posts (in the tuple 1=publish) it
    # is also filtering the created on date to show the most recent post at the top
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'my_articles.html'

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user).order_by('-created_on')

# DetailView gives a detailed view of a given object in the model at the specified template

class PostDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/users/accounts/login/'
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = BlogComment.objects.filter(
            blogpost_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        #likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        #total_likes=likes_connected.number_of_likes()
        #liked = False
        
        #if likes_connected.likes.filter(id=self.request.user.id).exists():
        #    liked = True
        #data['number_of_likes'] = total_likes
        #data['post_is_liked'] = liked
        if self.request.user.is_authenticated:
            data['comment_form'] = CommentForm(instance=self.request.user)

        return data
    
    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(content=request.POST.get('content'),
                                  author=self.request.user,
                                  blogpost_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
    

class PostCreate(LoginRequiredMixin, generic.CreateView):
    login_url = '/users/accounts/login/'
    model = Post
    template_name = 'post_form.html'
    fields = ['title','content', 'status']   
    
    def form_valid(self,form):
        # before saving the form, update some of the values
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    login_url = '/users/accounts/login/'
    model = Post
    template_name = 'post_form.html'
    # added slug incase user wants to change it from the default
    fields = ['title', 'slug', 'content', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # used by UserPassesTestMiin to ensure only the authr of the post can update it
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    login_url = '/users/accounts/login/'
    model = Post
    template_name = 'post_confirm_delete.html'
    # defines where to redirect the user after deleting the post
    success_url = '/'

    def test_func(self):
        # used by UserPassesTestMiin to ensure only the authr of the post can delete it
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
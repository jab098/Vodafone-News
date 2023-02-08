#importing the models class
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

#tuple to state whether an article is a draft or published version
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

#subclass of models.Model, called post containing the following attributes:
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    #image = models.ImageField(upload_to='blog_images',
                              #storage=gd_storage, null=True, blank=True)

    @property
    def number_of_comments(self):
        return BlogComment.objects.filter(blogpost_connected=self).count()

    #metadata stored in this class, the results will be sorted by the created on field
    class Meta:
        ordering = ['-created_on']

    #readable representation of the object
    def __str__(self):
        return self.author.username + ', ' + self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": str(self.slug)})
    
    def number_of_likes(self):
        return self.likes.count()

class BlogComment(models.Model):
    blogpost_connected = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #email = models.EmailField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author) + ', ' + self.blogpost_connected.title[:40]
    def get_absolute_url(self):
        # setting the redirect url, passing in the primary key
        return reverse('post_detail', kwargs={'slug':self.slug})

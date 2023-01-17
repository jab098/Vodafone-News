#importing the models class
from django.db import models
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
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    #metadata stored in this class, the results will be sorted by the created on field
    class Meta:
        ordering = ['-created_on']

    #readable representation of the object
    def __str__(self):
        return self.title


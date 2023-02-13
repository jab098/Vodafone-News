#importing the models class
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#tuple defining the status of the request
STATUS = (
    (0,"Submitted"),
    (1,"Accepted"),
    (-1,"Rejected")
)

#subclass of models.Model, called post containing the following attributes:
class WriteRequest(models.Model):
    id = models.AutoField(primary_key=True)
    requestee = models.ForeignKey(User, on_delete= models.CASCADE,related_name='requestee')
    created_on = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=200)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    #metadata stored in this class, the results will be sorted by the created on field
    class Meta:
        ordering = ['-created_on']

    def get_absolute_url(self):
        # setting the redirect url, passing in the primary key
        return reverse('home')

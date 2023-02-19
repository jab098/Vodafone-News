from .models import BlogComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        #defines the fields that will be in the comment form
        fields = ('author', 'content')
        # shows that the author of the comment wont be shown to the user, as it will be set to whoever writes the comment
        exclude = ('author',)
        labels = {
            # set the label for the content field to empty (we dont want this showing on the front end, just the input)
            "content":""
        }
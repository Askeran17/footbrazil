from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """ Form class for users to comment on a post """
    class Meta:
        model = Comment
        fields = ('text_comments',)


class AddPostForm(forms.ModelForm):
    """ Form class for superuser to add a post """
    class Meta:
        model = Post
        exclude = ['author', 'date', 'slug', 'status']

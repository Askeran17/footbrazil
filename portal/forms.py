from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text_comments',)

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'date', 'slug', 'status']

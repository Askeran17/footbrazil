from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# Models for app
class Post(models.Model):
    """
    Model class for posts in app
    """
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    featured_image = CloudinaryField('image', default='dfy0one9z', blank=True)
    description = models.TextField(default='')
    summary = models.TextField(blank=True)
    sponsor = models.CharField(default='Embratel', max_length=100)
    has_sponsor = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    date = models.DateField('Publication date', default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Model class for comments in app
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    text_comments = models.TextField('Texts field', max_length=2000)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.text_comments} by {self.author}"



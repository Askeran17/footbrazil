from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Models for app
class Post(models.Model):
    """
    Model class for posts in app
    """
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(default='')
    summary = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    date = models.DateField('Publication date') 

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

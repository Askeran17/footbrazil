from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """ Admin class to add post from admin panel """
    list_display = ('title', 'slug',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


admin.site.register(Comment)
""" to manage comments from admin panel """
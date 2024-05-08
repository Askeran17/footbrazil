from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Post

# Create your views here.

class PostView(View):
    '''show posts'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'templates/base.html', {'post_list': posts})
        paginate_by = 6
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View
from .forms import CommentForm
from .models import Post

# Create your views here.

class PostView(View):
    '''show posts'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'portal/index.html', {'post_list': posts})
        paginate_by = 6

class PostDetail(View):
    '''full detailed posts'''
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()

                return redirect('full_post', slug=post.slug)
        else:
            comment_form = CommentForm()

        return render(request, 'portal/full_post.html', {'post': post, 'comment_form': comment_form})

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return redirect(reverse('full_post', args=[slug]))
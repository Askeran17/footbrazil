from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CommentForm, AddPostForm
from .models import Post, Comment


# App views

class PostView(CreateView):
    '''show posts'''
    def get(self, request):
        posts = Post.objects.filter(status=1)
        return render(request, 'portal/index.html', {'post_list': posts})
        paginate_by = 6

def history(request):
    return render(request, 'portal/history.html')

def about(request):
    return render(request, 'portal/about.html')

def view_404(request, exception):
      return render(request, '404.html')

def full_post(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`portal/full_post.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )

    comment_form = CommentForm()

    return render(
        request,
        "portal/full_post.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return redirect(reverse('full_post', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return redirect(reverse('full_post', args=[slug]))


class AddPostView(CreateView):
    '''add post from the website itself'''
    model = Post
    template_name = 'portal/add_post.html'
    success_url = reverse_lazy("add_post")
    form = AddPostForm

    def get (self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "form" : self.form,
        })

    def post (self, request, *args, **kwargs):
        new_post_form = AddPostForm(request.POST, request.FILES)
        if new_post_form.is_valid():
            new_post = new_post_form.save(commit=False)
            new_post.author = request.user
            if request.user.is_superuser:
                new_post.status = 1
                new_post.save()
                messages.add_message(request, messages.SUCCESS, "Your post was added")
            else:
                messages.add_message(request, messages.ERROR, "Error adding post")
        else:
            new_post = self.form
        return redirect('home')

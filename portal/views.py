from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CommentForm, AddPostForm
from .models import Post, Comment


# App views
class PostView(CreateView):
    '''show posts'''
    def get(self, request):
        posts = Post.objects.filter(status=1)
        return render(request, 'portal/index.html', {'post_list': posts})


def history(request):
    return render(request, 'portal/history.html')


def about(request):
    return render(request, 'portal/about.html')


def view_404(request, exception):
    return render(request, '404.html')


def full_post(request, slug):
    """ Display detailed post """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
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
                'Comment submitted and awaiting approval')

    comment_form = CommentForm()

    return render(
        request,
        "portal/full_post.html",
        {"post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form, },
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
            messages.add_message(request, messages.ERROR, 'Error updating!')

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
        messages.add_message(request, messages.ERROR, 'Error delete!')

    return redirect(reverse('full_post', args=[slug]))


class AddPostView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    '''admin can add post from the website itself'''
    model = Post
    template_name = 'portal/add_post.html'
    form = AddPostForm

    def test_func(self):
        '''Test function to ensure user is admin'''
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "form": self.form,
        })

    def post(self, request, *args, **kwargs):
        new_post_form = AddPostForm(request.POST, request.FILES)
        if new_post_form.is_valid():
            new_post = new_post_form.save(commit=False)
            new_post.author = request.user
            new_post.status = 1
            new_post.save()
            messages.add_message(request, messages.SUCCESS, "Post was added")
        else:
            new_post = self.form
            messages.add_message(request, messages.ERROR, "Error adding post")
        return redirect('home')


class EditPost(UpdateView):
    '''admin can edit post from the website itself'''
    model = Post
    template_name = 'portal/edit_post.html'
    fields = (
        'title', 'slug', 'featured_image', 'description', 'summary', 'sponsor',
        'has_sponsor')
    success_url = reverse_lazy('home')


class DeletePost(DeleteView):
    '''admin can delete post from the website itself'''
    model = Post
    template_name = 'portal/delete_post.html'
    success_url = reverse_lazy('home')
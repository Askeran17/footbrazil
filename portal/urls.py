from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.PostView.as_view(), name='home'),
    path("add_post/", views.AddPostView.as_view(), name='add_post'),
    path(
        'post/edit_post/<int:pk>', views.EditPost.as_view(), name='edit_post'),
    path(
        'post/<int:pk>/delete_post', views.DeletePost.as_view(),
        name='delete_post'),
    path("history/", views.history, name='history'),
    path("about/", views.about, name='about'),
    path("accounts/", include("allauth.urls")),
    path('<slug:slug>/', views.full_post, name='full_post'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]

handler404 = 'portal.views.view_404'
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.PostView.as_view(), name='home'),
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
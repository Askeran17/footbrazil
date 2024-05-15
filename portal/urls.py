from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.PostView.as_view(), name='home'),
    path("accounts/", include("allauth.urls")),
    path('<slug:slug>/', views.PostDetail.as_view()),
]
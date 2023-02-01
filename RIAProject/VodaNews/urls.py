from . import views
from django.urls import path
from .views import BlogPostLike

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blogpost-like/<int:pk>/', views.BlogPostLike, name="blogpost_like"),
    #path('blogpost-detail/<int:pk>/', views.BlogPostLike, name="blogpost_detail"),
]

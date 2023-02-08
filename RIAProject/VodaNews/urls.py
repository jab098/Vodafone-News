from . import views
from django.urls import path
from .views import LikeView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<str:slug>/', LikeView, name="like_post"),
    #path('blogpost-detail/<int:pk>/', views.BlogPostLike, name="blogpost_detail"),
]

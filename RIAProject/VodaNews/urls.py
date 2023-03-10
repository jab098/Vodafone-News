from . import views
from django.urls import path
from .views import LikeView

# defines the urls relative to the ip address/domain name (path set for this project is empty)
urlpatterns = [
    # using class based views
    path('', views.PostList.as_view(), name='home'),
    path('posts/add/', views.PostCreate.as_view(), name='post-add'),
    path('posts/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/<str:slug>/like/', LikeView, name="like_post"),
    path('posts/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('posts/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('search_posts', views.search_posts, name='search_posts'),
    path('my_articles', views.MyPostList.as_view(), name='my_articles')
]

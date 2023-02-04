from . import views
from django.urls import path

urlpatterns = [
    # using class based views
    path('', views.PostList.as_view(), name='home'),
    path('add/', views.PostCreate.as_view(), name='post-add'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]

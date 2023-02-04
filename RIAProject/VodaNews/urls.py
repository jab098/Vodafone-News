from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add/', views.PostCreate.as_view(), name='add'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

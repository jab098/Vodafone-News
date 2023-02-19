from . import views
from django.urls import path, include
from .views import UserEditView

# defines the urls relative to the /users as defined in the base urls file
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('request-write/', views.requestWriterPermissions, name='request-writer'),
    path('my_account/', UserEditView.as_view(), name='my_account')
]

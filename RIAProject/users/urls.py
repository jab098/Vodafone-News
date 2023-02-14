from . import views
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('request-write/', views.requestWriterPermissions, name='request-writer')
]

from django.contrib import admin
from django.urls import path, include

# defines the urls within the app relative to the ip address/domain name
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('VodaNews.urls')),
    # Add Django site authentication urls (for login, logout, password management)
    path('users/', include('users.urls')),
    path('',include('pwa.urls'))
]

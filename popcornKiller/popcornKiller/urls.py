from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boxoffice.urls')),
    path('posts/', include('posts.urls')),
    path('rest-auth/', include('users.urls')),
]

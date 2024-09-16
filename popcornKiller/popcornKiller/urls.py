from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pk_apps.box_office.urls')),
    path('accounts/', include('pk_apps.accounts.urls')),
    path('diaries/', include('pk_apps.diaries.urls')),
]

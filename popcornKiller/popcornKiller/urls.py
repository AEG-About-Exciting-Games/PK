from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.box_office.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('diaries/', include('apps.diaries.urls')),
]

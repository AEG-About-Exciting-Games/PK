from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pk_apps.box_office.urls')),
    path('accounts/', include('pk_apps.accounts.urls')),
    path('diaries/', include('pk_apps.diaries.urls')),
]


# 개발 환경에서만 미디어 파일 서빙
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

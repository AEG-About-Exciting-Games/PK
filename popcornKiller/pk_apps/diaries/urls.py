from django.urls import path
from .views import diary_list, diary_detail, diary_create, diary_update, diary_delete

app_name = 'diaries'

urlpatterns = [
    path('', diary_list, name='diary_list'),
    path('<int:pk>/', diary_detail, name='diary_detail'),
    path('create/', diary_create, name='diary_create'),
    path('<int:pk>/edit/', diary_update, name='diary_update'),
    path('<int:pk>/delete/', diary_delete, name='diary_delete'),
]

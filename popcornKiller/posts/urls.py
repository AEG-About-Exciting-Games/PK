from django.urls import path
from .views import create_view, list_view, detail_view, update_view, delete_view

urlpatterns = [
    path('write/', create_view),  # create
    path('', list_view),  # read - list
    path('{int:id}/', detail_view),  # read - detail
    path('{int:id}/', update_view),  # update
    path('{int:id}/', delete_view),  # delete
]

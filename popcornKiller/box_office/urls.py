from django.urls import path

from .views import daily_view, movie_detail

urlpatterns = [
    path('', daily_view),
    path('movie_detail/', movie_detail, name='movie_detail'),
]

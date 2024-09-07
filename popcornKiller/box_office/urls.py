from django.urls import path

from .views import daily_view, movie_detail, actor_detail, search_list

app_name = 'box_office'

urlpatterns = [
    path('', daily_view, name='daily_view'),
    path('movie_detail/', movie_detail, name='movie_detail'),
    path('actor_detail/', actor_detail, name='actor_detail'),
    path('search_list/', search_list, name='search_list'),
]

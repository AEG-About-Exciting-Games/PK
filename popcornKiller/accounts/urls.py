from django.urls import path

from .views import signup, login_view, logout_view, update_view, unsubscribe_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('update/', update_view, name='update'),
    path('unsubscribe/', unsubscribe_view, name='unsubscribe'),
]

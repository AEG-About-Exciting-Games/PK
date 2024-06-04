from django.urls import path
from .views import register, login

urlpatterns = [
    path('registration/', register),
    path('login/', login),
    # path('logout/', ),
    # path('user/', ),
    # path('password/change/', ),
]

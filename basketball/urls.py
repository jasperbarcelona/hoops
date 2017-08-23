from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/new/', views.create_user, name='create_user'),
    url(r'^users/get/', views.get_user, name='get_user'),
    url(r'^game/new/', views.create_game, name='create_game'),
]
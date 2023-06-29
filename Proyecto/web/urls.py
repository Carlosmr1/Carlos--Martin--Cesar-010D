from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('index',views.index, name='index'),
    path('juegos/', views.juegos, name='juegos'),
    path('juegosMesa', views.tableGames, name='juegosMesa')
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('juegos/', views.juegos, name='juegos'),
    path('juegosMesa/', views.tableGames, name='juegosMesa'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('newCuenta/', views.newCuenta, name='newCuenta'),
    path('nosotros/', views.nosotros, name='nosotros'),
]
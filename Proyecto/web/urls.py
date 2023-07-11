from django.urls import path
from . import views
from .views import agregar_producto, eliminar_producto, limpiar_carrito, registro, restar_producto

urlpatterns = [
    path('',views.index, name='index'),
    path('juegos/', views.juegos, name='juegos'),
    path('juegosMesa/', views.tableGames, name='juegosMesa'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('newCuenta/', views.newCuenta, name='newCuenta'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('newCuenta/',registro.as_view(), name='newCuenta'),
    path('agregar/<str:producto_nombre>', agregar_producto, name='add'),
    path('eliminar/<str:producto_nombre>', eliminar_producto, name='delete'),
    path('restar/<str:producto_nombre>', restar_producto, name='rest'),
    path('limpiar/', limpiar_carrito, name='clear'),
    path('carrito/',views.carrito, name='carro'),
]
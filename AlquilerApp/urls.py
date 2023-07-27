from django.urls import path
from AlquilerApp import views

urlpatterns = [
    path('alquiler/',views.alquiler,name='Alquiler'),
    path('clientes/',views.clientes,name='Clientes'),
    path('clienteFormulario/',views.clienteFormulario,name='ClienteFormulario'),
    path('productoFormulario/',views.productoFormulario,name='ProductoFormulario'),
    path('buscarProductos/',views.buscarProductos,name='BuscarProductos'),
    path('busqueda/',views.busqueda),
]

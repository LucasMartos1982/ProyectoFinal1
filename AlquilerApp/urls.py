from django.urls import path
from AlquilerApp import views

urlpatterns = [
    path('alquiler/',views.alquiler,name='Alquiler'),
    path('clientes/',views.clientes,name='Clientes'),
    path('clienteFormulario/',views.clienteFormulario,name='ClienteFormulario'),
    #path('productoFormulario/',views.productoFormulario,name='ProductoFormulario'),
    path('buscarProductos/',views.buscarProductos,name='BuscarProductos'),
    path('busqueda/',views.busqueda,name='buscar_alquiler'),
    path('leerClientes/',views.leerClientes, name="LeerClientes"),
    path('leerArticulos/',views.leerArticulos, name="LeerArticulos"),
    path('eliminaCliente/<cliente_name>',views.eliminaCliente, name="EliminaCliente"),
    path('eliminaArticulo/<art_name>',views.eliminaArticulo, name="EliminaArticulo"),
    path('editarArticulo/<art_name>',views.editarArticulo, name="EditarArticulo"),
]

from django.urls import path,include
from EstenopoApp import views


urlpatterns = [
    path('',views.home,name='Home'),
    path('producto/',views.prod,name='Producto'),
    path('social/',views.soc,name='Social'),
    path('moda/',views.mod,name='Moda'),
    path('aerea/',views.ae,name='Aerea'),
    path('AlquilerApp/',include('AlquilerApp.urls')),
    path('login/',views.login_request,name='Login'),
    path('editarPerfil/',views.editarPerfil, name='EditarPerfil'),
    path('registro/',views.registro,name="Registro"),
    path('moda/list',views.ModaList.as_view(),name='MList'),
    path('moda/<pk>',views.ModaDetalle.as_view(),name='MDetail'),
    path('moda/nuevo/',views.ModaCreacion.as_view(),name='MNew'),
    path('moda/editar/<pk>',views.ModaUpdate.as_view(),name='MEdit'),
    path('moda/delete/<pk>',views.ModaDelete.as_view(),name='MDelete'),
    path('about/',views.about,name='About')    
]
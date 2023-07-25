from django.urls import path,include
from EstenopoApp import views


urlpatterns = [
    path('',views.home,name='Home'),
    path('producto/',views.prod,name='Producto'),
    path('social/',views.soc,name='Social'),
    path('moda/',views.mod,name='Moda'),
    path('aerea/',views.ae,name='Aerea'),
    path('AlquilerApp/',include('AlquilerApp.urls')),
]
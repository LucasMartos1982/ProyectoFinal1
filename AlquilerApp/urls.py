from django.urls import path
from AlquilerApp import views

urlpatterns = [
    path('alquiler/',views.alquiler,name='Alquiler'),
    path('clientes/',views.clientes,name='Clientes'),
    
]

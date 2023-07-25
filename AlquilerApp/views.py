from django.shortcuts import render
from django.http import HttpResponse
from AlquilerApp.models import Alquiler,Cliente
# Create your views here.

def alquila(self):
    prod=Alquiler(item='Tripode',cod='ET001',precio='$/h: 1000')
    prod.save()
    doctexto=f'Item: {prod.item} <br> Codigo: {prod.cod} <br> Precio: {prod.precio}'
    return HttpResponse(doctexto)

def alquiler(request):
    return render(request,'AlquilerApp/alquiler.html')

def clientes(request):
    return render(request,'AlquilerApp/clientes.html')


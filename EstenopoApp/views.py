from django.shortcuts import render
from django.http import HttpResponse
from EstenopoApp.models import Producto,Moda,Aerea,Social
# Create your views here.

def home(request):
    return render(request,'EstenopoApp/home.html')

def prod(request):
    return render(request,'EstenopoApp/producto.html')

def soc(request):
    return render(request,'EstenopoApp/social.html')

def mod(request):
    return render(request,'EstenopoApp/moda.html')

def ae(request):
    return render(request,'EstenopoApp/aerea.html')
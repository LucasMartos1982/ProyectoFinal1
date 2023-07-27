from django.shortcuts import render
from django.http import HttpResponse
from AlquilerApp.models import Alquiler,Cliente
from AlquilerApp.forms import ClienteFormulario, ProductosFormulario
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

def clienteFormulario(request):
    
    if request.method =="POST":
        
        myform=ClienteFormulario(request.POST)
        print(myform)
        
        if myform.is_valid:
            
            info=myform.cleaned_data
            cliente=Cliente(nombre=info['nombre'],apellido=info['apellido'],email=info['email'])
            cliente.save()
            return render(request, "AlquilerApp/clientes.html")
    else:
        myform=ClienteFormulario()
        
        return render(request,'AlquilerApp/clienteFormulario.html',{'myform':myform})

def productoFormulario(request):
    
    if request.method =="POST":
        
        myform=ProductosFormulario(request.POST)
        print(myform)
        
        if myform.is_valid:
            
            info=myform.cleaned_data
            prod=Alquiler(item=info['item'],cod=info['cod'],precio=info['precio'])
            prod.save()
            return render(request, "AlquilerApp/productoFormulario.html")
    else:
        myform=ProductosFormulario()
        
        return render(request,'AlquilerApp/productoFormulario.html',{'myform':myform})
    
def buscarProductos(request):
    return render(request,'AlquilerApp/buscarProducto.html')

def busqueda(request):
     
     if request.GET['item']:
         
         item=request.GET['item']
         cod=Alquiler.objects.filter(item_icontains=item)
         precio=Alquiler.objects.filter(item_icontains=item)
         
         return render(request,'alquiler.html',{'item':item,'cod':cod,'precio':precio})
     
     else:
         
         rta= 'No hay datos'
         
     return HttpResponse(rta)
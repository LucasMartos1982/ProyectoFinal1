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

#def alquiler(request):
 #   return render(request,'AlquilerApp/alquiler.html')

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

def alquiler(request):
    
    if request.method =="POST":
        
        myform=ProductosFormulario(request.POST)
        print(myform)
        
        if myform.is_valid:
            
            info=myform.cleaned_data
            prod=Alquiler(item=info['item'],cod=info['cod'],precio=info['precio'])
            prod.save()
            return render(request, "AlquilerApp/alquiler.html")
    else:
        myform=ProductosFormulario()
        
        return render(request,'AlquilerApp/alquiler.html',{'myform':myform})
    
def buscarProductos(request):
    return render(request,'AlquilerApp/buscarProducto.html')

def busqueda(request): 
    
    if 'item' in request.GET:
        item=request.GET['item']
        cod=Alquiler.objects.filter(item_icontains=item)
        precio=Alquiler.objects.filter(item_icontains=item)
         
        return render(request,'AlquilerApp/alquiler.html',{'item':item,'cod':cod,'precio':precio})
    
    return render(request,'AlquilerApp/buscarProducto.html')

# CRUD read 

def leerClientes(request):
    
    clientes=Cliente.objects.all()
    contexto={'clientes':clientes}
    
    return render(request,'AlquilerApp/leerClientes.html',contexto)

def leerArticulos(request):
    
    articulos=Alquiler.objects.all()
    contexto={'articulos':articulos}
    
    return render(request,'AlquilerApp/leerArticulos.html',contexto)

# CRUD delete

def eliminaCliente(request,cliente_name):
    
    cliente=Cliente.objects.get(nombre=cliente_name)
    cliente.delete()
    
    clientes=Cliente.objects.all()
    contexto={'clientes':clientes}
    
    return render(request,'AlquilerApp/leerClientes.html',contexto)

def eliminaArticulo(request,art_name):
    
    articulo=Alquiler.objects.get(item=art_name)
    articulo.delete()
    
    articulos=Alquiler.objects.all()
    contexto={'articulos':articulos}
    
    return render(request,'AlquilerApp/leerArticulos.html',contexto)

#CRUD edit

def editarArticulo(request,art_name):
    articulo=Alquiler.objects.get(item=art_name)
    
    if request.method=='POST':
        myForm=ProductosFormulario(request.POST)
        print(myForm)
        
        if myForm.is_valid:
            info=myForm.cleaned_data
            
            articulo.item=info['item']
            articulo.cod=info['cod']
            articulo.precio=info['precio']
            articulo.save()
            
            return render(request,'AlquilerApp/alquiler.html')
    else:
        myForm=ProductosFormulario(initial={'item':articulo.item, 'cod':articulo.cod, 'precio':articulo.precio})
        
    return render(request,'AlquilerApp/editarArticulo.html',{'myForm':myForm,'art_name':art_name})
            
        
        





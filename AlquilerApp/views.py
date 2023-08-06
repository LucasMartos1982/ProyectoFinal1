from django.shortcuts import render,redirect
from django.http import HttpResponse
from AlquilerApp.models import Alquiler,Cliente
from AlquilerApp.forms import ClienteFormulario, ProductosFormulario,AlqForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required 
def estudio(request):
    return render(request,'AlquilerApp/estudio.html') 

@login_required
def alquiler(request):
    return render(request,'AlquilerApp/alquiler.html')
    
@login_required
def clientes(request):
    print(f'hola : {request.user.is_staff}')
    return render(request,'AlquilerApp/clientes.html') 


def alquiler(request):
    
    if request.method =="POST":
        
        myForm=ProductosFormulario(request.POST)
        print(myForm)
        
        if myForm.is_valid:
            
            info=myForm.cleaned_data
            prod=Alquiler(item=info['item'],cod=info['cod'],precio=info['precio'])
            prod.save()
            return render(request, "AlquilerApp/alquiler.html")
    else:
        myForm=ProductosFormulario()
        
        return render(request,'AlquilerApp/alquiler.html',{'myForm':myForm})
              
#---------- Vistas basadas en clases Cliente -------------------

class ClienteList(ListView):
    model=Cliente
    template_name="AlquilerApp/cliente_list.html"

class ClienteDetalle(DetailView):
    model=Cliente
    template_name="AlquilerApp/cliente_detalle.html"
    
class ClienteCreacion(CreateView):
    model=Cliente
    success_url=reverse_lazy('List')
    fields=['nombre', 'apellido', 'email'] 
    
class ClienteUpdate(UpdateView):
    model=Cliente
    success_url=reverse_lazy('List')
    fields=['nombre', 'apellido', 'email'] 
    
class ClienteDelete(DeleteView):
    model=Cliente
    success_url=reverse_lazy('List')
    
#---------- Vistas basadas en clases Articulos -------------------
    
class ArticulosList(ListView):
    model=Alquiler
    template_name="AlquilerApp/articulos_list.html"

class ArticulosDetalle(DetailView):
    model=Alquiler
    template_name="AlquilerApp/articulos_detalle.html"
    
class ArticulosCreacion(CreateView):
    model=Alquiler
    success_url=reverse_lazy('Art_List')
    fields=['item', 'cod', 'Descripcion','Autor','fecha','precio','imagen'] 
    
class ArticulosUpdate(UpdateView):
    model=Alquiler
    success_url=reverse_lazy('Art_List')
    fields=['item', 'cod', 'Descripcion','Autor','fecha','precio','imagen'] 
    
class ArticulosDelete(DeleteView):
    model=Alquiler
    success_url=reverse_lazy('Art_List')


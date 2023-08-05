from django.shortcuts import render
from django.http import HttpResponse
from AlquilerApp.models import Alquiler,Cliente
from AlquilerApp.forms import ClienteFormulario, ProductosFormulario
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
    #articulos=Alquiler.objects.all()
    #contexto={'articulos':articulos}
    return render(request,'AlquilerApp/alquiler.html')
    #return render(request,'AlquilerApp/alquiler.html',contexto)
    
@login_required
def clientes(request):
    print(f'hola : {request.user.is_staff}')
    return render(request,'AlquilerApp/clientes.html') 

#def clienteFormulario(request):
    
    #if request.method =="POST":
        
        #myForm=ClienteFormulario(request.POST)
        #print(myForm)
        
        #if myForm.is_valid:
            
            #info=myForm.cleaned_data
            #cliente=Cliente(nombre=info['nombre'],apellido=info['apellido'],email=info['email'])
            #cliente.save()
            #return render(request, "AlquilerApp/clientes.html")
    #else:
        #myForm=ClienteFormulario()
        
        #return render(request,'AlquilerApp/clienteFormulario.html',{'myform':myForm})


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
    
def buscarProductos(request):
    return render(request,'AlquilerApp/alquiler.html')

def busqueda(request): 
    
    if request.GET['item']:
        item=request.GET['item']
        codigo=Alquiler.objects.filter(item_icontains=item)
        precio=Alquiler.objects.filter(item_icontains=item)
         
        return render(request,'AlquilerApp/estudio.html',{'item':item,'cod':codigo,'precio':precio})
    else:
        rta='No hay datos'
    return render(request,'AlquilerApp/estudio.html',{'respuesta':rta})

# CRUD read 

#def leerClientes(request):
    
    #clientes=Cliente.objects.all()
    #contexto={'clientes':clientes}
    
    #return render(request,'AlquilerApp/clientes.html',contexto)

#def leerArticulos(request):
    
    #articulos=Alquiler.objects.all()
    #contexto={'articulos':articulos}
    
    #return render(request,'AlquilerApp/leerArticulos.html',contexto)

# CRUD delete

#def eliminaCliente(request,cliente_name):
    
    #cliente=Cliente.objects.get(nombre=cliente_name)
    #cliente.delete()
    
    #clientes=Cliente.objects.all()
    #contexto={'clientes':clientes}
    
    #return render(request,'AlquilerApp/leerClientes.html',contexto)

#def eliminaArticulo(request,art_name):
    
    #articulo=Alquiler.objects.get(item=art_name)
    #articulo.delete()
    
    #articulos=Alquiler.objects.all()
    #contexto={'articulos':articulos}
    
    #return render(request,'AlquilerApp/leerArticulos.html',contexto)

#CRUD edit

#def editarArticulo(request,art_name):
    #articulo=Alquiler.objects.get(item=art_name)
    
    #if request.method=='POST':
        #myForm=ProductosFormulario(request.POST)
        #print(myForm)
        
        #if myForm.is_valid:
            #info=myForm.cleaned_data
            
            #articulo.item=info['item']
            #articulo.cod=info['cod']
            #articulo.precio=info['precio']
            #articulo.save()
            
            #return render(request,'AlquilerApp/alquiler.html')
    #else:
        #myForm=ProductosFormulario(initial={'item':articulo.item, 'cod':articulo.cod, 'precio':articulo.precio})
        
    #return render(request,'AlquilerApp/editarArticulo.html',{'myForm':myForm,'art_name':art_name})
            
#def editarCliente(request,cliente_name):
    #cliente=Cliente.objects.get(name=cliente_name)
    
    #if request.method=='POST':
        #myForm=ClienteFormulario(request.POST)
        #print(myForm)
        
        #if myForm.is_valid:
            #info=myForm.cleaned_data
            
            #cliente.nombre=info['nombre']
            #cliente.apellido=info['apellido']
            #cliente.email=info['email']
            #cliente.save()
            
            #return render(request,'AlquilerApp/clientes.html')
    #else:
        #myForm=ClienteFormulario(initial={'nombre':cliente.nombre, 'apellido':cliente.apellido, 'email':cliente.email})
        
    #return render(request,'AlquilerApp/editarCliente.html',{'myForm':myForm,'cliente_name':cliente_name})      
        
#---------- Vistas basadas en clases Cliente -------------------

class ClienteList(ListView):
    model=Cliente
    template_name="AlquilerApp/cliente_list.html"

class ClienteDetalle(DetailView):
    model=Cliente
    template_name="AlquilerApp/cliente_detalle.html"
    
class ClienteCreacion(CreateView):
    model=Cliente
    success_url="AlquilerApp/clientes"
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
    success_url="AlquilerApp/alquiler"
    fields=['item', 'cod', 'precio'] 
    
class ArticulosUpdate(UpdateView):
    model=Alquiler
    success_url=reverse_lazy('Art_List')
    fields=['item','cod','precio'] 
    
class ArticulosDelete(DeleteView):
    model=Alquiler
    success_url=reverse_lazy('Art_List')



#def login_request(request):
    
    #if request.method=="POST":
        #form=AuthenticationForm(request, data= request.POST)
        
        #if form.is_valid():
            #usuario=form.cleaned_data.get('username')
            #contrasena=form.cleaned_data.get('password')
            
            #user=authenticate(username=usuario,password=contrasena)
            
    '''if user is not None:
                login(request,user)
                return render(request,'AlquilerApp/estudio.html',{'mensaje':f'Bienvenido! {usuario}'})
            else:
                return render(request,'AlquilerApp/estudio.html',{'mensaje':'Error, datos incorrectos'})
        else:
            return render(request,'AlquilerApp/estudio.html',{'mensaje':'formulario erroneo'})
        
    form=AuthenticationForm()   
    return render(request,'AlquilerApp/login.html',{'form':form})'''
            
'''def registro(request):
    
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,'AlquilerApp/estudio.html',{'mensaje':'Usuario Creado'})
    else:
        form=UserRegisterForm()
        return render(request,'AlquilerApp/registro.html',{'form':form})'''
            
'''@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        myForm = UserEditForm(request.POST)

        if myForm.is_valid():

            info = myForm.cleaned_data

            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.last_name = info['last_name']
            usuario.first_name = info['first_name']

            usuario.save()

            return render(request, "AlquilerApp/alquiler.html")

    else:

        myForm = UserEditForm(initial={'email':usuario.email})

    return render(request, "AlquilerApp/editarPerfil.html", {"myForm": myForm, "usuario": usuario})'''

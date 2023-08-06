from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from EstenopoApp.models import Producto,Moda,Aerea,Social
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from EstenopoApp.forms import UserEditForm,UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


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

def login_request(request):
    
    if request.method=="POST":
        form=AuthenticationForm(request, data= request.POST)
        
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contrasena=form.cleaned_data.get('password')
            
            user=authenticate(username=usuario,password=contrasena)
            
            if user is not None:
                login(request,user)
                return render(request,'AlquilerApp/estudio.html',{'mensaje':f'Bienvenido! {usuario}'})
            else:
                return render(request,'EstenopoApp/errorLogin.html',{'mensaje':'Error, datos incorrectos'})
        else:
            return render(request,'EstenopoApp/errorLogin.html',{'mensaje':'formulario erroneo'})
        
    form=AuthenticationForm()   
    return render(request,'EstenopoApp/login.html',{'form':form})

@login_required
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

            return render(request, "EstenopoApp/home.html")

    else:

        myForm = UserEditForm(initial={'email':usuario.email})

    return render(request, "EstenopoApp/editarPerfil.html", {"myForm": myForm, "usuario": usuario})

def registro(request):
    
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,'EstenopoApp/reg.html',{'mensaje':'Usuario Creado'})
        else:
            return render(request,'EstenopoApp/registro.html',{'form':form})
    else:
        form=UserRegisterForm()
        return render(request,'EstenopoApp/registro.html',{'form':form})
    
    
class ModaList(ListView):
    model=Moda
    template_name="EstenopoApp/moda_list.html"

class ModaDetalle(DetailView):
    model=Moda
    template_name="EstenopoApp/moda_detalle.html"
    
class ModaCreacion(CreateView):
    model=Moda
    success_url="/EstenopoApp/moda"
    fields=['nombre_moda', 'precio_moda'] 
    
class ModaUpdate(UpdateView):
    model=Moda
    success_url=reverse_lazy('MList')
    fields=['nombre_moda', 'precio_moda'] 
    
class ModaDelete(DeleteView):
    model=Moda
    success_url=reverse_lazy('MList')
    
    
def about(request):
    return render(request,'EstenopoApp/about.html')
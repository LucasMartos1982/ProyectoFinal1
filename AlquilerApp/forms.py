from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class ClienteFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()    
    
class ProductosFormulario(forms.Form):
    item=forms.CharField(max_length=60)
    cod=forms.CharField(max_length=20)
    precio=forms.FloatField()


class AlqForm(forms.ModelForm):
 
    class Meta:
        model = Alquiler
        fields = ['item', 'cod', 'Descripcion','Autor','fecha','precio','imagen']

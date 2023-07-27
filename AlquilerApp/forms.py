from django import forms

class ClienteFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()    
    
class ProductosFormulario(forms.Form):
    item=forms.CharField(max_length=60)
    cod=forms.CharField(max_length=20)
    precio=forms.FloatField()
    
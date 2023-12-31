from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    nombre_prod=models.CharField(max_length=100)
    precio_prod=models.FloatField()
    
    def __str__(self):
        return f'Fotografia de Producto: {self.nombre_prod} - Precio: {self.precio_prod}'
    
class Moda(models.Model):
    nombre_moda=models.CharField(max_length=100)
    precio_moda=models.FloatField()
    foto=models.ImageField(upload_to='Moda', null=True, blank = True)
    
    def __str__(self):
        return f'Fotografia de Moda: {self.nombre_moda} - Precio: {self.precio_moda}'
    
class Social(models.Model):
    nombre_social=models.CharField(max_length=100)
    precio_social=models.FloatField()
    
    def __str__(self):
        return f'Fotografia Social: {self.nombre_social} - Precio: {self.precio_social}'
    
class Aerea(models.Model):
    nombre_aerea=models.CharField(max_length=100)
    precio_aerea=models.FloatField()
    
    def __str__(self):
        return f'Fotografia Aerea: {self.nombre_aerea} - Precio: {self.precio_aerea}'
    
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='media/avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"
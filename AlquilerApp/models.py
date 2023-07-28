from django.db import models

# Create your models here.

class Alquiler(models.Model):
    item=models.CharField(max_length=60)
    cod=models.CharField(max_length=60)
    precio=models.FloatField(max_length=20)
    
    def __str__(self):
        return f'Item: {self.item} - Cod: {self.cod} - Precio $/hs: {self.precio}'
    
class Cliente(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}'

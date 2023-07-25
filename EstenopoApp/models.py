from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre_prod=models.CharField(max_length=100)
    precio_prod=models.FloatField()
    
class Moda(models.Model):
    nombre_moda=models.CharField(max_length=100)
    precio_moda=models.FloatField()
    
class Social(models.Model):
    nombre_social=models.CharField(max_length=100)
    precio_social=models.FloatField()
    
class Aerea(models.Model):
    nombre_aerea=models.CharField(max_length=100)
    precio_aerea=models.FloatField()
   
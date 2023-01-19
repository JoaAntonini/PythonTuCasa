from django.db import models

# Create your models here.
class Sillon(models.Model):
    nombre=models.CharField(max_length=40)
    precio = models.IntegerField()    
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Precio {self.precio}"


class Lamparas(models.Model):
    nombre=models.CharField(max_length=40)
    precio = models.IntegerField()    
    tamaño = models.CharField(max_length=40)
    
    def __str__(self):
            return f"Nombre: {self.nombre} - Precio {self.precio} - Tamaño {self.tamaño}"

class Mesas(models.Model):
    nombre=models.CharField(max_length=40)
    precio = models.IntegerField()    
    color= models.CharField(max_length=40)
    
    def __str__(self):
            return f"Nombre: {self.nombre} - Precio {self.precio} - Color {self.color}"
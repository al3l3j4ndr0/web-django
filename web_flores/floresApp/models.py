from django.db import models

class producto(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=50)
    precio=models.IntegerField()

    def __str__(self):
        return self.nombre

class cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self):
        return self.nombre

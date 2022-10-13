from django.db import models

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    raza = models.CharField(max_length=200)
    personalidad = models.CharField(max_length=200)
    edad = models.CharField(max_length=200)
    tamaño = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    historial = models.TextField()
    foto = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
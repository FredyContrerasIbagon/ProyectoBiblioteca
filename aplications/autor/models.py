from django.db import models

from .managers import AutorManager

# Create your models here.

class Autor(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20)
    edad = models.PositiveIntegerField()

    objects = AutorManager()

    def __str__(self):
        return self.nombres + ' - ' + self.apellidos

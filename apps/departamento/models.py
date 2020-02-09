from django.db import models
from django.urls import reverse_lazy, reverse


class Departamento(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self): #esta funcion nos trae el valor del objeto en vez del nombre del objeto cuando es llave foranea o forekeing
		return self.nombre

	def get_absolute_url(self):
	    return reverse('index')

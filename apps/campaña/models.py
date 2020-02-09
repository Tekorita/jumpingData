from django.db import models
from django.urls import reverse_lazy, reverse


class Campaña(models.Model):
	nombre = models.CharField(max_length=50)
	
	def get_absolute_url(self):
	    return reverse('index')

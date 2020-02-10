from django.db import models
from django.urls import reverse_lazy, reverse

from apps.sede.models import Sede


class Afiliador(models.Model):
    id_afiliador = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    sede = models.ForeignKey(Sede, null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('index')

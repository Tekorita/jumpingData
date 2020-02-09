from django.db import models
from django.urls import reverse_lazy, reverse

from apps.campaña.models import Campaña
from apps.departamento.models import Departamento
from apps.distrito.models import Distrito

class Sede(models.Model):
    campaña = models.ForeignKey(Campaña, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, null=True, blank=True, on_delete=models.CASCADE)
    direccion = models.TextField()

    def get_absolute_url(self):
        return reverse('index')

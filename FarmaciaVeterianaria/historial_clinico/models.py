# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Paciente.models import Paciente
from inventario.models import Producto


class Historia(models.Model):
    paciente = models.ForeignKey(Paciente, null=False ,blank=False, on_delete=models.CASCADE)
    fecha_historial = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    descripcion_historia = models.TextField(max_length=800, blank=True, null=True)
    producto = models.ManyToManyField(Producto ,blank=False)

    def __str__(self):
        return self.paciente

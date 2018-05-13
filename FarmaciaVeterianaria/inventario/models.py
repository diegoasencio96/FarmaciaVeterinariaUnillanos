# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=45, blank=False, null=False)

    def __str__(self):
        return self.nombre_paciente

class Procedimiento(models.Model):
    nombre_procedimiento = models.CharField(max_length=60, blank=False, null=False)
    paciente = models.ForeignKey(Paciente, null=False ,blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_procedimiento

class TipoProducto(models.Model):
    nombre_tipo_producto = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.nombre_tipo_producto
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=60, blank=False, null=False)
    tipoproduct = models.ForeignKey(TipoProducto, null=False ,blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto
    
class Historial(models.Model):
    fecha_historial = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    producto = models.ManyToManyField(Producto ,blank=False)
    paciente = models.ForeignKey(Paciente, null=False ,blank=False, on_delete=models.CASCADE)
    
      
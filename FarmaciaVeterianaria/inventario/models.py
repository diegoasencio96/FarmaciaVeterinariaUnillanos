# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=45, blank=False, null=False)

class Historial(models.Model):
    fecha_historial = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
      
class Procedimiento(models.Model):
    nombre_procedimiento = models.CharField(max_length=60, blank=False, null=False)

class TipoMedicamento(models.Model):
    nombre_tipomedicamento = models.CharField(max_length=60, blank=False, null=False)
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=60, blank=False, null=False)
    

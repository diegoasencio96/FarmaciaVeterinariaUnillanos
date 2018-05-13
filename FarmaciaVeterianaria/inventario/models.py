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
    SMLV = models.FloatField()
    precio = models.IntegerField()
    paciente = models.ForeignKey(Paciente, null=False ,blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_procedimiento

class TipoProducto(models.Model):
    nombre_tipo_producto = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.nombre_tipo_producto

class FormaFarmaceutica(models.Model):
    nombre_forma_farmaceutica = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.nombre_forma_farmaceutica

class Laboratorio(models.Model):
    nombre_laboratorio = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.nombre_laboratorio

class PresentacionUnidad(models.Model):
    nombre_presentacion_unidad = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.nombre_presentacion_unidad
    
class Producto(models.Model):
    tipo_producto = models.ForeignKey(TipoProducto, null=False ,blank=False, on_delete=models.CASCADE)

    referencia_comercial = models.CharField(max_length=60, blank=False, null=False)
    nombre_comercial = models.CharField(max_length=60, blank=False, null=False)
    nombre_generico = models.CharField(max_length=60, blank=False, null=False)
    forma_farmaceutica = models.ForeignKey(FormaFarmaceutica, null=False ,blank=False, on_delete=models.CASCADE)
    concentracion = models.CharField(max_length=60, blank=False, null=False)
    laboratorio = models.ForeignKey(Laboratorio, null=False ,blank=False, on_delete=models.CASCADE)
    presentacion_cantidad = models.CharField(max_length=60, blank=False, null=False)
    presentacion_unidad = models.ForeignKey(PresentacionUnidad, null=False ,blank=False, on_delete=models.CASCADE)
    precio = models.IntegerField()
    indicaciones = models.TextField(max_length=200, blank=False, null=False)
    principal_indicacion = models.CharField(max_length=60, blank=False, null=False)
    lote = models.CharField(max_length=60, blank=False, null=False)
    invima = models.CharField(max_length=60, blank=False, null=False)
    fecha_de_vencimiento = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    cantidad_existentes = models.IntegerField()


    def __str__(self):
        return self.referencia_comercial
    
class Historial(models.Model):
    paciente = models.ForeignKey(Paciente, null=False ,blank=False, on_delete=models.CASCADE)
    fecha_historial = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    descripcion_historia = models.TextField(max_length=800, blank=True, null=True)
    producto = models.ManyToManyField(Producto ,blank=False)
    
      
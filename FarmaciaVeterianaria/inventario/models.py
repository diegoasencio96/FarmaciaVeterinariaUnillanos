# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Paciente.models import Paciente

# Create your models here.


class TipoProducto(models.Model):
    nombre_tipo_producto = models.CharField(max_length=60, blank=False, null=False)
    descripcion_tipo_producto = models.TextField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.nombre_tipo_producto

class FormaFarmaceutica(models.Model):
    nombre_forma_farmaceutica = models.CharField(max_length=60, blank=False, null=False)
    descripcion_forma_farmaceutica = models.TextField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.nombre_forma_farmaceutica

class Laboratorio(models.Model):
    nombre_laboratorio = models.CharField(max_length=60, blank=False, null=False)
    descripcion_del_laboratorio = models.TextField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return self.nombre_laboratorio

class PresentacionUnidad(models.Model):
    nombre_presentacion_unidad = models.CharField(max_length=10, blank=False, null=False)
    descripcion_presentacion_unidad = models.TextField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.nombre_presentacion_unidad

    class Meta:
        verbose_name_plural = 'Presentanción de unidades'

class PresentacionCantidad(models.Model):
    nombre_presentacion_cantidad = models.CharField(max_length=10, blank=False, null=False)
    descripcion_presentacion_cantidad = models.TextField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.nombre_presentacion_cantidad

    class Meta:
        verbose_name_plural = 'Presentanción de cantidades'
    
class Producto(models.Model):
    tipo_producto = models.ForeignKey(TipoProducto, null=False ,blank=False, on_delete=models.CASCADE)
    referencia_comercial = models.CharField(max_length=60, blank=False, null=False)
    nombre_comercial = models.CharField(max_length=60, blank=False, null=False)
    nombre_generico = models.CharField(max_length=60, blank=False, null=False)
    forma_farmaceutica = models.ForeignKey(FormaFarmaceutica, null=False ,blank=False, on_delete=models.CASCADE)
    concentracion = models.CharField(max_length=60, blank=False, null=False)
    laboratorio = models.ForeignKey(Laboratorio, null=False ,blank=False, on_delete=models.CASCADE)
    presentacion_cantidad = models.ForeignKey(PresentacionCantidad, null=False ,blank=False, on_delete=models.CASCADE)
    presentacion_unidad = models.ForeignKey(PresentacionUnidad, null=False ,blank=False, on_delete=models.CASCADE)
    precio = models.IntegerField()
    indicaciones = models.TextField(max_length=200, blank=False, null=False)
    principal_indicacion = models.CharField(max_length=60, blank=False, null=False)
    lote = models.CharField(max_length=60, blank=False, null=False)
    invima = models.CharField(max_length=60, blank=False, null=False)
    fecha_de_vencimiento = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    cantidad_existentes = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.referencia_comercial
    

    
      
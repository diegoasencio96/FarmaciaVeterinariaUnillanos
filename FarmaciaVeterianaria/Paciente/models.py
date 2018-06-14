# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Especie(models.Model):
    nombre_especie = models.CharField(max_length=60, blank=False, null=False)
    descripcion_especie = models.TextField(max_length=300, blank=True, null=True)

    def __unicode__(self):
        return self.nombre_especie

class Raza(models.Model):
    nombre_raza = models.CharField(max_length=60, blank=False, null=False)
    descripcion_raza = models.TextField(max_length=300, blank=True, null=True)

    def __unicode__(self):
        return self.nombre_raza

class Medico(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length = 60,blank = False, null=False)
    apellidos = models.CharField(max_length=60, blank = False, null=False)
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField(verbose_name= 'Número de contacto')
    profesion = models.CharField(max_length = 60,blank = False, null=False)

    def __unicode__(self):
        return self.nombres+' '+self.apellidos

class Propietario(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length = 60,blank = False, null=False)
    apellidos = models.CharField(max_length=60, blank = False, null=False)
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField(verbose_name= 'Número de contacto')
    direccion = models.CharField(max_length=40,blank=True, null=True)

    def __unicode__(self):
        return self.nombres+' '+self.apellidos


class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=75, blank=False, null=False, verbose_name = 'Nombre del paciente')
    especie = models.ForeignKey(Especie, verbose_name='Especie', null=False, blank = False, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, verbose_name='Raza', null=False, blank = False, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso')
    motivo_consulta = models.TextField(verbose_name='Motivo de la consulta', null=True, blank=False)
    medico_tratante = models.ForeignKey(Medico, verbose_name='Medico tratante', null=True, blank = True, on_delete=models.CASCADE)
    #num_historia_clinica = models.ForeignKey()
    fk_propietario = models.ForeignKey(Propietario, verbose_name='Propietario', null=True, blank = False, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre_paciente
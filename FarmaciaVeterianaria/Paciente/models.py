# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Propietario(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length = 25,blank = False)
    apellidos = models.CharField(max_length=40, blank = False)
    correo = models.EmailField(blank=True)
    telefono = models.IntegerField(verbose_name= 'Número de contacto')

    def __str__(self):
        return self.cedula


class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=75, blank=False, null=False, verbose_name = 'Nombre del paciente')
    especie = models.CharField(max_length=75, blank=False, null=True)
    raza = models.CharField(max_length=75, blank=False, null=True)
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso')
    motivo_consulta = models.TextField(verbose_name='Motivo de la consulta', null=True, blank=False)
    medica_tratante = models.CharField(max_length=75, verbose_name='Medico tratante', blank=False, null=True)
    #num_historia_clinica = models.ForeignKey()
    fk_propietario = models.ForeignKey(Propietario, verbose_name='Propietario', null=True, blank = False)

    def __str__(self):
        return self.nombre_paciente
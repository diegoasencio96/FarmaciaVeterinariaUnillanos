# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Paciente.models import Paciente


class Procedimiento(models.Model):
    nombre_procedimiento = models.CharField(max_length=60, blank=False, null=False)
    SMLV = models.FloatField()
    precio = models.IntegerField()
    paciente = models.ForeignKey(Paciente, null=False ,blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_procedimiento
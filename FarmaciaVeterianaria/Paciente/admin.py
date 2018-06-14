# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Paciente.models import Paciente, Propietario, Especie, Raza, Medico

admin.site.register(Paciente)
admin.site.register(Propietario)
admin.site.register(Especie)
admin.site.register(Raza)
admin.site.register(Medico)
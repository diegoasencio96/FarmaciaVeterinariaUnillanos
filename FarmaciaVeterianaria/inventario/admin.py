# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.

admin.site.register(TipoProducto)
admin.site.register(Producto)

admin.site.register(FormaFarmaceutica)
admin.site.register(Laboratorio)
admin.site.register(PresentacionUnidad)


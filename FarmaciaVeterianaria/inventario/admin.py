# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
from forms import *

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Historial)
admin.site.register(Procedimiento)
admin.site.register(TipoProducto)
admin.site.register(Producto)
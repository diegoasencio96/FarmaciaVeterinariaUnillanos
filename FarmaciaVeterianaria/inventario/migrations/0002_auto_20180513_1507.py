# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-13 20:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipoproducto',
            old_name='nombre_tipoproducto',
            new_name='nombre_tipo_producto',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-13 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_de_vencimiento',
            field=models.DateField(auto_now=True),
        ),
    ]
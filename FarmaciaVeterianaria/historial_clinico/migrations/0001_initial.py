# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 03:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0001_initial'),
        ('Paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_historial', models.DateTimeField(auto_now_add=True)),
                ('descripcion_historia', models.TextField(blank=True, max_length=800, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Paciente.Paciente')),
                ('producto', models.ManyToManyField(to='inventario.Producto')),
            ],
        ),
    ]

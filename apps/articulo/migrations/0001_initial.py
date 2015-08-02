# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
        ('subdepartamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('barras', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('costo', models.DecimalField(max_digits=6, decimal_places=2)),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
                ('oferta', models.DecimalField(max_digits=6, decimal_places=2)),
                ('fechaAlta', models.DateField()),
                ('estado', models.BooleanField()),
                ('proveedor', models.ForeignKey(to='proveedor.Proveedor')),
                ('subdepartamento', models.ForeignKey(to='subdepartamento.SubDepartamento')),
            ],
        ),
    ]

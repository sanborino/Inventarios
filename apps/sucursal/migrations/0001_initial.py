# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('municipio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('municipio', models.ForeignKey(to='municipio.Municipio')),
            ],
        ),
    ]

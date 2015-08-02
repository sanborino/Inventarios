from django.db import models
from apps.sucursal.models import Sucursal

class Departamento(models.Model):
	nombre = models.CharField(max_length=50)
	numero = models.CharField(max_length=50)
	sucursal = models.ForeignKey(Sucursal)

	def __unicode__(self):
		return "%s %s" % (self.nombre, self.sucursal.nombre)
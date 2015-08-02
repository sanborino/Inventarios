from django.db import models
from apps.municipio.models import Municipio

class Sucursal(models.Model):
	municipio = models.ForeignKey(Municipio)
	nombre = models.CharField(max_length=50)
	numero = models.IntegerField()
	direccion = models.CharField(max_length=200)
	telefono = models.IntegerField()
	correo = models.EmailField()

	def __unicode__(self):
		return self.municipio.nombre
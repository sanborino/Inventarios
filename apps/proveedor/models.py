from django.db import models
from apps.municipio.models import Municipio

class Proveedor(models.Model):
	nombre = models.CharField(max_length=50)
	numero = models.IntegerField()
	direccion = models.CharField(max_length=200)
	telefono = models.IntegerField()
	correo = models.EmailField()
	contacto = models.CharField(max_length=100)
	condiciones = models.CharField(max_length=50)
	numeroUnico = models.CharField(max_length=50)
	estado = models.BooleanField()
	municipio = models.ForeignKey(Municipio)

	def __unicode__(self):
		return self.nombre
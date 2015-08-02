from django.db import models
from apps.departamento.models import Departamento

class SubDepartamento(models.Model):
	nombre = models.CharField(max_length=50)
	numero = models.CharField(max_length=50)
	departamento = models.ForeignKey(Departamento)

	def __unicode__(self):
		return "%s %s" % (self.nombre,self.departamento)
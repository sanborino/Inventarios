from django.db import models

class tipoMovimiento(models.Model):
	nombre = models.CharField(max_length=50)
	codigo = models.CharField(max_length=5)

	def __unicode__(self):
		return "%s %s" % (self.codigo,self.nombre)
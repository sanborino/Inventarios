from django.db import models

class Detalle(models.Model):
	barras = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=50)
	piezas = models.IntegerField(max_length=10)
	costo = models.DecimalField(max_digits=6, decimal_places=2)

	def __unicode__(self):
		return self.barras
		
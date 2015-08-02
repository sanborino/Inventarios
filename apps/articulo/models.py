from django.db import models
from apps.subdepartamento.models import SubDepartamento
from apps.proveedor.models import Proveedor

class Articulo(models.Model):
	barras = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=50)
	modelo = models.CharField(max_length=50)
	costo = models.DecimalField(max_digits=6, decimal_places=2)
	precio = models.DecimalField(max_digits=6,decimal_places=2)
	oferta = models.DecimalField(max_digits=6,decimal_places=2)
	fechaAlta = models.DateField()
	estado = models.BooleanField()
	subdepartamento = models.ForeignKey(SubDepartamento)
	proveedor = models.ForeignKey(Proveedor)

	def __unicode__(self):
		return self.subdepartamento.nombre
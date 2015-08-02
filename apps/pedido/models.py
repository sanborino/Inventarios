from django.db import models
from apps.sucursal.models import Sucursal
from apps.tipoPedido.models import tipoPedido
from apps.proveedor.models import Proveedor
from apps.detalle.models import Detalle

class Pedido(models.Model):
	costo = models.DecimalField(max_digits=6, decimal_places=2)
	piezas = models.IntegerField(max_length=10)
	fechaElaboracion = models.DateField()
	fechaCancelacion = models.DateField()
	estado = models.CharField(max_length=20)
	sucursal = models.OneToOneField(Sucursal)
	tipoPedido = models.OneToOneField(tipoPedido)
	proveedor = models.OneToOneField(Proveedor)
	detalle = models.OneToOneField(Detalle)

	def __unicode__(self):
		return self.estado
		
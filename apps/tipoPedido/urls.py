from django.conf.urls import include, url
from .views import TipoPedido
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^tipoPedido/$', TipoPedido.as_view(), name="tipoPedido"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),

]
from django.conf.urls import include, url
from .views import TipoCompra
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^tipoCompra/$', TipoCompra.as_view(), name="tipoCompra"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),

]
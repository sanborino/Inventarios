from django.conf.urls import include, url
from .views import TipoTransferencia
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^tipoTransferencia/$', TipoTransferencia.as_view(), name="tipoTransferencia"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),

]
from django.conf.urls import include, url
from .views import TipoMovimiento
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^tipoMovimiento/$', TipoMovimiento.as_view(), name="tipoMovimiento"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),

]
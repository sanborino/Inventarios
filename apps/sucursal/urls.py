from django.conf.urls import include, url
from .views import RegistrarSucursal
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^sucursal/$', RegistrarSucursal, name="sucursal"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),
]
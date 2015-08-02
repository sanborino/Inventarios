from django.conf.urls import include, url
from .views import RegistrarProveedor
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^proveedor/$', RegistrarProveedor, name="proveedor"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),
]
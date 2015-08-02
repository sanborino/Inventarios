from django.conf.urls import include, url
from .views import RegistrarArticulo
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^articulo/$', RegistrarArticulo, name="articulo"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),
]
from django.conf.urls import include, url
from .views import TipoDevolucion
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^tipoDevolucion/$', TipoDevolucion.as_view(), name="tipoDevolucion"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),

]
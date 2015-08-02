from django.conf.urls import include, url
from .views import TipoAjuste
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^tipoAjuste/$', TipoAjuste.as_view(), name="tipoAjuste"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),

]
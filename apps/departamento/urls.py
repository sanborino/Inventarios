from django.conf.urls import include, url
from .views import RegistrarDepartamento
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^departamento/$', RegistrarDepartamento, name="departamento"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),
]
from django.conf.urls import include, url
from .views import RegistrarSubDepartamento
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^subdepartamento/$', RegistrarSubDepartamento, name="subdepartamento"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),
]
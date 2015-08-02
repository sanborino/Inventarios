from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import tipoCompra
from django.core.urlresolvers import reverse_lazy

class TipoCompra(CreateView):
	template_name = 'administracion/tipoCompra.html'
	model = tipoCompra
	fields = '__all__'
	success_url = reverse_lazy('confirma')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TipoCompra, self).dispatch(*args, **kwargs)
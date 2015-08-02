from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import tipoTransferencia
from django.core.urlresolvers import reverse_lazy

class TipoTransferencia(CreateView):
	template_name = 'administracion/tipoTransferencia.html'
	model = tipoTransferencia
	fields = '__all__'
	success_url = reverse_lazy('confirma')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TipoTransferencia, self).dispatch(*args, **kwargs)
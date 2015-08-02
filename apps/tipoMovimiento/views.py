from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import tipoMovimiento
from django.core.urlresolvers import reverse_lazy

class TipoMovimiento(CreateView):
	template_name = 'administracion/tipoMovimiento.html'
	model = tipoMovimiento
	fields = '__all__'
	success_url = reverse_lazy('confirma')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TipoMovimiento, self).dispatch(*args, **kwargs)
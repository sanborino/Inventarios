from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import tipoPedido
from django.core.urlresolvers import reverse_lazy

class TipoPedido(CreateView):
	template_name = 'administracion/tipoPedido.html'
	model = tipoPedido
	fields = '__all__'
	success_url = reverse_lazy('confirma')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TipoPedido, self).dispatch(*args, **kwargs)
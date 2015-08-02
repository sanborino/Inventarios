from django.shortcuts import render_to_response
from forms import DepartamentoForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def RegistrarDepartamento(request):
	if request.method == 'POST':
		form = DepartamentoForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/localidad/confirma/')

	else:
		form = DepartamentoForm()

	return render_to_response('negocio/departamento.html',{'form':form},
		context_instance=RequestContext(request))
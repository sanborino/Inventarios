from django.shortcuts import render_to_response
from forms import SubDepartamentoForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def RegistrarSubDepartamento(request):
	if request.method == 'POST':
		form = SubDepartamentoForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/localidad/confirma/')

	else:
		form = SubDepartamentoForm()

	return render_to_response('negocio/subdepartamento.html',{'form':form},
		context_instance=RequestContext(request))
from django.shortcuts import render_to_response
from .models import Sucursal
from forms import SucursalForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def RegistrarSucursal(request):
	if request.method == 'POST':
		form = SucursalForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/localidad/confirma/')
	else:
		form = SucursalForm()

	return render_to_response('negocio/sucursal.html',{'form':form},
		context_instance=RequestContext(request))
from django.shortcuts import render_to_response
from forms import ProveedorForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def RegistrarProveedor(request):
	if request.method == 'POST':
		form = ProveedorForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/localidad/confirma/')

	else:
		form = ProveedorForm()

	return render_to_response('negocio/proveedor.html',{'form':form},
		context_instance=RequestContext(request))
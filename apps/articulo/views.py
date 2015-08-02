from django.shortcuts import render_to_response
from forms import ArticuloForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def RegistrarArticulo(request):
	if request.method == 'POST':
		form = ArticuloForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/localidad/confirma/')

	else:
		form = ArticuloForm()

	return render_to_response('negocio/articulo.html',{'form':form},
		context_instance=RequestContext(request))
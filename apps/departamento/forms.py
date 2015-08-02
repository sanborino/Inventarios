from django import forms
from .models import Departamento

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('nombre', 'numero', 'sucursal')

    def __init__(self, *args, **kwargs):
    	super(DepartamentoForm, self).__init__(*args, **kwargs)
    	self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['numero'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['sucursal'].widget.attrs.update({'class' : 'form-control'})
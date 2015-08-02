from django import forms
from .models import SubDepartamento

class SubDepartamentoForm(forms.ModelForm):
    class Meta:
        model = SubDepartamento
        fields = ('nombre', 'numero', 'departamento')

    def __init__(self, *args, **kwargs):
    	super(SubDepartamentoForm, self).__init__(*args, **kwargs)
    	self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['numero'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['departamento'].widget.attrs.update({'class' : 'form-control'})
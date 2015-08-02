from django import forms
from .models import Sucursal

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ('nombre','numero','direccion','telefono','correo','municipio')

    def __init__(self, *args, **kwargs):
    	super(SucursalForm, self).__init__(*args, **kwargs)
    	self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['numero'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['direccion'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['telefono'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['correo'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['municipio'].widget.attrs.update({'class' : 'form-control'})
    
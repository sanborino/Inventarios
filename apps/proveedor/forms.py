from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('nombre','numero','direccion','telefono','correo','contacto','condiciones','numeroUnico',
            'estado','municipio')

    def __init__(self, *args, **kwargs):
    	super(ProveedorForm, self).__init__(*args, **kwargs)
    	self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['numero'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['direccion'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['telefono'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['correo'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['contacto'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['condiciones'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['numeroUnico'].widget.attrs.update({'class' : 'form-control'})
        self.fields['estado'].widget.attrs.update({'class' : 'form-control'})
        self.fields['municipio'].widget.attrs.update({'class' : 'form-control'})
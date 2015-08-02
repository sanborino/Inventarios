from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ('subdepartamento','proveedor','barras','descripcion','modelo','costo',
            'precio','oferta','estado')

    def __init__(self, *args, **kwargs):
    	super(ArticuloForm, self).__init__(*args, **kwargs)
    	self.fields['subdepartamento'].widget.attrs.update({'class' : 'form-control'})
        self.fields['proveedor'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['barras'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['descripcion'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['modelo'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['costo'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['precio'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['oferta'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['estado'].widget.attrs.update({'class' : 'form-control'})
    	
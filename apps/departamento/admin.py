from django.contrib import admin
from .models import Departamento

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','numero','sucursal')

admin.site.register(Departamento,DepartamentoAdmin)
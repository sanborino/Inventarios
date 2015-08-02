from django.contrib import admin
from .models import SubDepartamento

class SubDepartamentoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','numero','departamento')

admin.site.register(SubDepartamento,SubDepartamentoAdmin)
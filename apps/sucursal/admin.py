from django.contrib import admin
from .models import Sucursal

class SucursalAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','municipio')

admin.site.register(Sucursal,SucursalAdmin)

from django.contrib import admin
from alquilatec.models import Equipo, Alquiler, EquipoAlquiler
# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio', 'creado', 'actualizado']
admin.site.register(Equipo, EquipoAdmin)


class EquipoAlquilerAdmin(admin.TabularInline):
    model = EquipoAlquiler

class AlquilerAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'inicia', 'termina', 'status']
    inlines = [EquipoAlquilerAdmin]
admin.site.register(Alquiler, AlquilerAdmin)

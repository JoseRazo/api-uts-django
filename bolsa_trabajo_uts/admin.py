from django.contrib import admin

# Register your models here.

from .models import Categoria, Descripcion, FormatoReferencia, Vacante


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Descripcion)
class DescripcionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(FormatoReferencia)
class FormatoReferenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'archivo', 'fecha_creacion', 'fecha_actualizacion')


@admin.register(Vacante)
class VacanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'descripcion', 'activo', 'fecha_creacion', 'fecha_actualizacion')

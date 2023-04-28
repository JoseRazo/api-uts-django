from django.contrib import admin
from becas.models import Institucion, Beca, Convocatoria

class BecaInline(admin.StackedInline):
    model = Beca
    verbose_name = 'Beca'
    verbose_name_plural = 'Becas'
    extra = 0

@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    inlines = (BecaInline,)
    list_display = ('nombre', 'url', 'activo', 'fecha_creacion')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

@admin.register(Beca)
class BecaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'institucion', 'activo', 'fecha_creacion')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

@admin.register(Convocatoria)
class ConvocatoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'activo', 'fecha_creacion')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')





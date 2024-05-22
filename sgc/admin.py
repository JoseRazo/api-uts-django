from django.contrib import admin
from .models import Departamento, Categoria, Documento

# Define TabularInline for Documento
class DocumentoInline(admin.TabularInline):
    model = Documento

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    inlines = [
        DocumentoInline,
    ]

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'revision', 'archivo', 'departamento', 'fecha', 'fecha_actualizacion','creado_por','actualizado_por')
    list_filter = ('departamento', 'categoria')
    search_fields = ('nombre', 'codigo', 'revision')
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        # Asigna el usuario actual al guardar el documento
        if not obj.pk:
            obj.creado_por = request.user
        obj.save(user=request.user)

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Documento, DocumentoAdmin)

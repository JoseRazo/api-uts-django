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
    list_display = ('nombre', 'codigo', 'revision', 'archivo', 'departamento', 'fecha', 'fecha_actualizacion')
    list_filter = ('departamento', 'categoria')
    search_fields = ('nombre', 'codigo', 'revision')
    list_per_page = 20

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Documento, DocumentoAdmin)

from django.contrib import admin
from noticias.models import Articulo, Categoria, ArticuloImagen

# Register your models here.

class ImagenInline(admin.TabularInline):
    model = ArticuloImagen
    verbose_name = 'Imagen para Slider'
    verbose_name_plural = 'Imágenes para Slider'

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'fecha_evento', 'fecha_creacion')
    prepopulated_fields = {'slug': ('titulo',)}
    inlines = (ImagenInline,)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.save()
    

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

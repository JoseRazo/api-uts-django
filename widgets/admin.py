from django.contrib import admin

from widgets.models import Carousel, CarouselItem, CarouselItemFile

class CarouselItemFileInline(admin.TabularInline):
    model = CarouselItemFile
    extra = 1
    verbose_name = "Archivo del Item"
    verbose_name_plural = "Archivos del Item"
    fields = ('nombre', 'archivo')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    can_delete = True
    show_change_link = True

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre',)
    ordering = ('-fecha_creacion',)
    fieldsets = (
        (None, {
            'fields': ('nombre', 'fecha_creacion', 'fecha_actualizacion')
        }),
    )
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'carousel', 'activo', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre',)
    ordering = ('-fecha_creacion',)
    list_filter = ('activo',)
    fieldsets = (
        (None, {
            'fields': ('nombre', 'carousel', 'imagen', 'url', 'target', 'activo', 'fecha_creacion', 'fecha_actualizacion')
        }),
    )
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    inlines = [CarouselItemFileInline]

admin.site.register(Carousel, CarouselAdmin)
admin.site.register(CarouselItem, CarouselItemAdmin)
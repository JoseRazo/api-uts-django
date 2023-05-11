from django.contrib import admin
from eventos.models import Instructor,Cronograma,Hotel,Patrocinadores,Header,Evento,Curso

# Register your models here.
class CursoInLine(admin.StackedInline):
    model=Curso
    extra=2

class InstructorAdmin(admin.ModelAdmin):
    inlines=[CursoInLine]
    list_display=("nombre","correo","area_estudios","fotografia")
    search_fields=("nombre","correo","area_estudios")

class CronogramaAdmin(admin.ModelAdmin):
    list_display=("actividad","dia","hora")
    search_fields=("actividad","dia","hora")

class HotelAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","url")

class PatrocinadoresAdmin(admin.ModelAdmin):
    list_display=("nombre","url")

class HeaderAdmin(admin.ModelAdmin):
    list_display=("seccion","url_seccion")

class EventoAdmin(admin.ModelAdmin):
    list_display=("nombre","lugar","descripcion")
    search_fields=("nombre","lugar","descripcion")

class CursoAdmin(admin.ModelAdmin):
    list_display=("nombre","instructor","objetivo")
    search_fields=("nombre","instructor","objetivo")

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Cronograma, CronogramaAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Patrocinadores, PatrocinadoresAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Curso, CursoAdmin)
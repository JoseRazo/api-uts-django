from django.contrib import admin
from eventos.models import Instructor,Cronograma,Hotel,Patrocinadores,Header,Evento

# Register your models here.
class InstructorAdmin(admin.ModelAdmin):
    list_display=("nombre","correo","area_estudios")
    search_fields=("nombre","correo","area_estudios")

class CronogramaAdmin(admin.ModelAdmin):
    list_display=("actividad","dia","hora")
    search_fields=("actividad","dia","hora")

class HotelAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion")

class PatrocinadoresAdmin(admin.ModelAdmin):
    list_display=("nombre","url")

class HeaderAdmin(admin.ModelAdmin):
    list_display=("seccion","url_seccion")

class EventoAdmin(admin.ModelAdmin):
    list_display=("nombre","lugar","descripcion")
    search_fields=("nombre","lugar","descripcion")

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Cronograma, CronogramaAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Patrocinadores, PatrocinadoresAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Evento, EventoAdmin)

from django.contrib import admin
from eventos.models import Instructor,Cronograma,Hotel,Patrocinadores,Header,Evento,Curso,Empresa,Registro

# Register your models here.
class CursoInLine(admin.StackedInline):
    model=Curso
    extra=2

class InstructorAdmin(admin.ModelAdmin):
    inlines=[CursoInLine]
    list_display=("nombre","correo","area_estudios","fotografia")
    search_fields=("nombre","correo","area_estudios")

class CronogramaAdmin(admin.ModelAdmin):
    list_display=("id", "tipo_actividad", "curso", "dia","fecha","hora_inicio","hora_fin")
    search_fields=("id", "tipo_actividad", "curso", "dia","fecha","hora_inicio","hora_fin")

class HotelAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","url")

class PatrocinadoresAdmin(admin.ModelAdmin):
    list_display=("nombre","url")

class HeaderAdmin(admin.ModelAdmin):
    list_display=("seccion","url_seccion","seccion_id")

class EventoAdmin(admin.ModelAdmin):
    list_display=("nombre","lugar","activo")
    search_fields=("nombre","lugar","activo")

class CursoAdmin(admin.ModelAdmin):
    list_display=("nombre","instructor","objetivo")
    search_fields=("nombre","instructor","objetivo")

class EmpresaAdmin(admin.ModelAdmin):
    list_display=("nombre",)
    search_fields=("nombre",)

class RegistroAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellido_paterno", "apellido_materno", "escuela_procedencia", "taller", "foto", "inscrito", "referencia", "comprobante_pago")
    search_fields=("nombre",)

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Cronograma, CronogramaAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Patrocinadores, PatrocinadoresAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Registro, RegistroAdmin)
# admin.site.register(Contacto, ContactoAdmin)

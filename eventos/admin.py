from django.contrib import admin
from import_export.widgets import ForeignKeyWidget
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin, ExportMixin
from eventos.models import (
    Instructor,
    Cronograma,
    Hotel,
    Patrocinadores,
    Header,
    Evento,
    Curso,
    Empresa,
    Registro
)

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
    search_fields=("id", "tipo_actividad", "curso__nombre", "dia","fecha","hora_inicio","hora_fin")

class HotelAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","url")

class PatrocinadoresAdmin(admin.ModelAdmin):
    list_display=("nombre",)

class HeaderAdmin(admin.ModelAdmin):
    list_display=("seccion","url_seccion","seccion_id")

class EventoAdmin(admin.ModelAdmin):
    list_display=("nombre","lugar","activo")
    search_fields=("nombre","lugar","activo")

class CursoResource(resources.ModelResource):
    class Meta:
        model = Curso
        fields = ('id', 'nombre',)
        export_order = ('id', 'nombre',)

class CursoAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = CursoResource
    list_display=("nombre", "instructor", "activo")
    search_fields=("nombre", "instructor__nombre")

class EmpresaAdmin(admin.ModelAdmin):
    list_display=("nombre", 'activo', 'visita_industrial')
    search_fields=("nombre",)

class RegistroResource(resources.ModelResource):
    id = fields.Field(attribute='id', column_name='ID', readonly=True)
    nombre = fields.Field(attribute='nombre', column_name='Nombre')
    apellido_paterno = fields.Field(attribute='apellido_paterno', column_name='Apellido Paterno')
    apellido_materno = fields.Field(attribute='apellido_materno', column_name='Apellido Materno')
    email = fields.Field(attribute='email', column_name='Email')
    tipo_participante = fields.Field(attribute='tipo_participante', column_name='Tipo Participante')
    universidad_empresa = fields.Field(attribute='universidad_empresa', column_name='Universidad o Empresa')
    matricula = fields.Field(attribute='matricula', column_name='Matricula')
    numero_empleado = fields.Field(attribute='numero_empleado', column_name='Numero de Empleado')
    taller = fields.Field(attribute='taller', column_name='Taller', widget=ForeignKeyWidget(Curso, 'nombre'))
    dia_taller = fields.Field(attribute='dia_taller', column_name='Dia Ingreso al taller')
    visita_industrial = fields.Field(attribute='visita_industrial', column_name='Visita Industrial', widget=ForeignKeyWidget(Empresa, 'nombre'))
    dia_visita = fields.Field(attribute='dia_visita', column_name='Dia Visita Industrial')
    inscrito = fields.Field(attribute='inscrito', column_name='Inscrito')
    referencia = fields.Field(attribute='referencia', column_name='Referencia')

    class Meta:
        model = Registro
        fields = ('id', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'tipo_participante',
                  'universidad_empresa', 'matricula', 'numero_empleado', 'taller', 'inscrito', 'referencia', 'fecha_creacion')
    
    def before_save_instance(self, instance, using_transactions, dry_run):
        taller_nombre = getattr(instance, 'taller')
        if taller_nombre:
            taller = Curso.objects.get(nombre=taller_nombre)
            instance.taller = taller
        return instance
    
    def before_save_instance(self, instance, using_transactions, dry_run):
        visita_nombre = getattr(instance, 'visita_industrial')
        if visita_nombre:
            visita_industrial = Empresa.objects.get(nombre=visita_nombre)
            instance.visita_industrial = visita_industrial
        return instance
    
    def before_import_row(self, row, **kwargs):
        tipo_participante_value = row.get('Tipo Participante')
        if tipo_participante_value:
            tipo_participante = next(item[0] for item in Registro.PARTICIPANTE_CHOICES if item[1] == tipo_participante_value)
            row['Tipo Participante'] = tipo_participante
        return super().before_import_row(row, **kwargs)


class RegistroAdmin(ImportExportModelAdmin):
    resource_class = RegistroResource
    list_display=("nombre_completo", 'email', 'tipo_participante', "universidad_empresa", "taller", "inscrito", "referencia", 'fecha_creacion')
    readonly_fields = ("fecha_creacion", "fecha_actualizacion")
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'referencia', 'email')
    list_filter = ('taller',)

    # def has_add_permission(self, request, obj=None):
    #     return False
        
    # def has_delete_permission(self, request, obj=None):
    #     return False

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

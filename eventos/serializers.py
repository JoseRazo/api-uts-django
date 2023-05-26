from rest_framework import serializers
from .models import Instructor,Cronograma,Hotel,Patrocinadores,Header,Evento,Curso, Empresa

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instructor
        fields = ('id','nombre','telefono','correo','area_estudios','descripcion','curriculum','fecha_creacion','fecha_actualizacion','fotografia')
        read_only_filds = ('id','nombre','telefono','correo','area_estudios','descripcion','curriculum','fecha_creacion','fecha_actualizacion','fotografia',)

class CursoSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()
    class Meta:
        model = Curso
        fields = ('id','instructor','nombre','objetivo')
        read_only_fields = ('id','instructor','nombre','objetivo',)

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('nombre',)
        read_only_fields = ('nombre',)

class CronogramaSerializer(serializers.ModelSerializer):
    curso = CursoSerializer()
    empresa = EmpresaSerializer()
    class Meta:
        model=Cronograma
        fields = ('id', 'tipo_actividad', 'curso', 'empresa', 'otra_actividad', 'dia', 'fecha', 'hora_inicio', 'hora_fin')
        read_only_fields = ('id', 'tipo_actividad', 'curso', 'empresa', 'otra_actividad', 'dia', 'fecha', 'hora_inicio', 'hora_fin')

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields = ('id','nombre','direccion','imagen','url',)
        read_only_fields = ('id','nombre','direccion','imagen',)

class PatrocinadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patrocinadores
        fields = ('id','nombre','logo','url')
        read_only_fields = ('id','nombre','logo','url',)

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ('id','seccion','url_seccion','seccion_id')
        read_only_fields = ('id','seccion','url_seccion','seccion_id')
 
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id','nombre','lugar','descripcion','mapa','logo','activo')
        read_only_fields = ('id','nombre','lugar','descripcion','mapa','logo','activo')
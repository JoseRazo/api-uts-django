from rest_framework import serializers
from .models import Instructor,Cronograma,Hotel,Patrocinadores,Header,Evento,Curso,Cronograma_Dia2

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instructor
        fields = ('id','nombre','telefono','correo','area_estudios','descripcion','curriculum','fecha_creacion','fecha_actualizacion','fotografia')
        read_only_filds = ('id','nombre','telefono','correo','area_estudios','descripcion','curriculum','fecha_creacion','fecha_actualizacion','fotografia',)

class CronogramaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cronograma
        fields = ('id','actividad','dia','hora_inicio','hora_fin','fotografia')
        read_only_fields = ('id','actividad','dia','hora_inicio','hora_fin','fotografia')

class Cronograma_Dia2Serializer(serializers.ModelSerializer):
    class Meta:
        model=Cronograma_Dia2
        fields = ('id','dia','hora','hora2','actividad','fotografia')
        read_only_fields = ('id','dia','hora','hora2','actividad','fotografia',)

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

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id','instructor','nombre','objetivo')
        read_only_fields = ('id','instructor','nombre','objetivo',)
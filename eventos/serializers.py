from rest_framework import serializers
from .models import Instructor,Cronograma,Hotel,Patrocinadores,Header,Evento,Curso

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instructor
        fields = ('id','nombre','telefono','correo','area_estudios','descripcion','curriculum','fecha_creacion','fecha_actualizacion','fotografia')
        read_only_filds = ('id','nombre','telefono','correo','area_estudios','descripcion','curriculum','fecha_creacion','fecha_actualizacion','fotografia',)

class CronogramaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cronograma
        fields = ('id','dia','hora','actividad','descripcion','fotografia')
        read_only_fields = ('id','dia','hora','actividad','descripcion','fotografia',)

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
        fields = ('id','seccion','url_seccion')
        read_only_fields = ('id','seccion','url_seccion',)
 
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id','nombre','lugar','descripcion','mapa','logo')
        read_only_fields = ('id','nombre','lugar','descripcion','mapa','logo',)

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id','instructor','nombre','objetivo')
        read_only_fields = ('id','instructor','nombre','objetivo',)
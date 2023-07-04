from django.conf import settings
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from .models import Instructor, Cronograma, Hotel, Patrocinadores, Header, Evento, Curso, Empresa, Registro

def update_image_url(image_url):
    # Verifica si la URL de la imagen comienza con "http://" y reemplázala por "https://"
    if image_url and image_url.startswith('http://') and not settings.DEBUG:
        updated_url = image_url.replace('http://', 'https://')
        return updated_url

    return image_url

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'nombre')
        read_only_fields = ('id', 'nombre')

class InstructorSerializer(serializers.ModelSerializer):
    cursos = CursosSerializer(many=True, read_only=True, source='curso_set')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['fotografia'] = update_image_url(representation['fotografia'])
        return representation
    
    class Meta:
        model=Instructor
        fields = ('id','nombre','telefono','correo','area_estudios','descripcion','curriculum','fecha_creacion','fecha_actualizacion','fotografia', 'cursos')
        read_only_filds = ('id','nombre','telefono','correo','area_estudios','descripcion','curriculum','fecha_creacion','fecha_actualizacion','fotografia', 'cursos')

class InstructorCursoSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['fotografia'] = update_image_url(representation['fotografia'])
        return representation
    
    class Meta:
        model=Instructor
        fields = ('id','nombre','telefono','correo','area_estudios','descripcion','curriculum','fecha_creacion','fecha_actualizacion','fotografia')
        read_only_filds = ('id','nombre','telefono','correo','area_estudios','descripcion','curriculum','fecha_creacion','fecha_actualizacion','fotografia')

class CursoSerializer(serializers.ModelSerializer):
    instructor = InstructorCursoSerializer()
    class Meta:
        model = Curso
        fields = ('id','instructor','nombre','objetivo')
        read_only_fields = ('id','instructor','nombre','objetivo',)

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id', 'nombre', 'visita_industrial', 'activo')
        read_only_fields = ('id', 'nombre', 'visita_industrial', 'activo')

class CronogramaSerializer(serializers.ModelSerializer):
    curso = CursoSerializer()
    empresa = EmpresaSerializer()
    class Meta:
        model=Cronograma
        fields = ('id', 'tipo_actividad', 'curso', 'empresa', 'otra_actividad', 'dia', 'fecha', 'hora_inicio', 'hora_fin')
        read_only_fields = ('id', 'tipo_actividad', 'curso', 'empresa', 'otra_actividad', 'dia', 'fecha', 'hora_inicio', 'hora_fin')

class HotelSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['imagen'] = update_image_url(representation['imagen'])
        return representation
    
    class Meta:
        model=Hotel
        fields = ('id','nombre','direccion','imagen','url',)
        read_only_fields = ('id','nombre','direccion','imagen',)

class PatrocinadoresSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['logo'] = update_image_url(representation['logo'])
        return representation
    
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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['logo'] = update_image_url(representation['logo'])
        return representation
    
    class Meta:
        model = Evento
        fields = ('id','nombre','lugar','descripcion','mapa','logo','activo')
        read_only_fields = ('id','nombre','lugar','descripcion','mapa','logo','activo')

class ContactoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    telefono = serializers.CharField(max_length=20, required=False)
    asunto = serializers.CharField(max_length=200)
    mensaje = serializers.CharField()

class RegistroSerializer(serializers.ModelSerializer):
    # taller = CursoSerializer()
    class Meta:
        model = Registro
        fields = (
            'id',
            'nombre',
            'apellido_paterno',
            'apellido_materno', 
            'email', 
            'tipo_participante', 
            'universidad_empresa', 
            'matricula', 
            'numero_empleado', 
            'taller',
            'dia_taller',
            'visita_industrial',
            'dia_visita', 
            'referencia', 
            'comprobante_pago',
            'formato_inscripcion',
            )
        read_only_fields = ('id',)

    def to_representation(self, instance):
        self.fields['taller'] =  CursoSerializer(read_only=True)
        return super(RegistroSerializer, self).to_representation(instance)
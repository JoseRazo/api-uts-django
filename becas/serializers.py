from django.conf import settings
from rest_framework import serializers
from .models import Institucion, Beca, Convocatoria

def update_archivo_url(archivo_url):
    # Verifica si la URL de la imagen comienza con "http://" y reemplázala por "https://"
    if archivo_url and archivo_url.startswith('http://') and not settings.DEBUG:
        updated_url = archivo_url.replace('http://', 'https://')
        return updated_url

    return archivo_url

class ConvocatoriaSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        # Obtiene la representación del objeto
        representation = super().to_representation(instance)
        
        # Actualiza las URLs de los archivos
        representation['archivo_convocatoria'] = update_archivo_url(representation['archivo_convocatoria'])
        representation['archivo_resultado'] = update_archivo_url(representation['archivo_resultado'])
        
        return representation
    
    class Meta:
        model = Convocatoria
        fields = '__all__'

class BecaSerializer(serializers.ModelSerializer):
    convocatorias = ConvocatoriaSerializer(many=True)
    
    class Meta:
        model = Beca
        # fields = '__all__'
        fields = ('id', 'nombre', 'descripcion', 'activo', 'fecha_creacion', 'fecha_actualizacion', 'convocatorias')

class InstitucionSerializer(serializers.ModelSerializer):
    becas = BecaSerializer(many=True)
    
    class Meta:
        model = Institucion
        # fields = '__all__'
        fields = ('id', 'nombre', 'url', 'activo', 'fecha_creacion', 'fecha_actualizacion', 'becas')
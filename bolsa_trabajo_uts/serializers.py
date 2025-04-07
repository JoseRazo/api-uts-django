from django.conf import settings
from rest_framework import serializers
from .models import Vacante, Categoria, Descripcion, FormatoReferencia

def update_archivo_url(archivo_url):
    # Verifica si la URL de la imagen comienza con "http://" y reemplázala por "https://"
    if archivo_url and archivo_url.startswith('http://') and not settings.DEBUG:
        updated_url = archivo_url.replace('http://', 'https://')
        return updated_url

    return archivo_url

class FormatoReferenciaSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['archivo'] = update_archivo_url(representation['archivo'])
        return representation
    
    class Meta:
        model = FormatoReferencia
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class DescripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descripcion
        fields = '__all__'

class VacanteSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    descripcion = DescripcionSerializer()
    formato_referencia = FormatoReferenciaSerializer()
    
    def to_representation(self, instance):
        # Obtiene la representación del objeto
        representation = super().to_representation(instance)
        
        # Actualiza las URLs de los archivos
        representation['convocatoria'] = update_archivo_url(representation['convocatoria'])
        representation['resultados'] = update_archivo_url(representation['resultados'])
        
        return representation
    
    class Meta:
        model = Vacante
        fields = '__all__'


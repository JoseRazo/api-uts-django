from django.conf import settings
from rest_framework import serializers
from .models import Articulo, ArticuloImagen


class ArticuloImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticuloImagen
        fields = '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    imagenes = ArticuloImagenSerializer(many=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Obtén la URL de la imagen del objeto actual
        imagen_url = representation['imagen']

        # Verifica si la URL comienza con "http://" y reemplázala por "https://"
        if imagen_url.startswith('http://') and not settings.DEBUG:
            imagen_url = imagen_url.replace('http://', 'https://')

        # Actualiza la URL de la imagen en la representación
        representation['imagen'] = imagen_url

        # Verifica si hay imágenes adicionales
        if 'imagenes' in representation and not settings.DEBUG:
            for imagen_data in representation['imagenes']:
                imagen_url = imagen_data['imagen']

                # Verifica si la URL comienza con "http://" y reemplázala por "https://"
                if imagen_url.startswith('http://'):
                    imagen_url = imagen_url.replace('http://', 'https://')

                # Actualiza la URL de la imagen en la representación de cada objeto ArticuloImagen
                imagen_data['imagen'] = imagen_url

        return representation

    class Meta:
        model = Articulo
        # fields = '__all__'
        fields = ('id', 'titulo', 'contenido', 'slug', 'imagen', 'fecha_evento', 'categoria', 'usuario', 'fecha_creacion', 'fecha_actualizacion', 'imagenes')
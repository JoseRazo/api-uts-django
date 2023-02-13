from rest_framework import serializers
from .models import Articulo, ArticuloImagen


class ArticuloImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticuloImagen
        fields = '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    imagenes = ArticuloImagenSerializer(many=True)
    class Meta:
        model = Articulo
        # fields = '__all__'
        fields = ('id', 'titulo', 'contenido', 'slug', 'imagen', 'fecha_evento', 'categoria', 'usuario', 'fecha_creacion', 'fecha_actualizacion', 'imagenes')
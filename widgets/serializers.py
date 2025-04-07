from rest_framework import serializers
from .models import CarouselItem, CarouselItemFile

class CarouselItemFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItemFile
        fields = ['id', 'nombre', 'archivo']

class CarouselItemSerializer(serializers.ModelSerializer):
    archivos = CarouselItemFileSerializer(many=True, read_only=True)

    class Meta:
        model = CarouselItem
        fields = ['id', 'nombre', 'imagen', 'url', 'target', 'activo', 'archivos']

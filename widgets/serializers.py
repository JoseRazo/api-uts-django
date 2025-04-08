from rest_framework import serializers
from .models import CarouselItem, CarouselItemFile
from core.utils import update_url_in_representation

class CarouselItemFileSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return update_url_in_representation(representation, 'archivo')
    
    class Meta:
        model = CarouselItemFile
        fields = ['id', 'nombre', 'archivo']

class CarouselItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return update_url_in_representation(representation, 'imagen')
    
    archivos = CarouselItemFileSerializer(many=True, read_only=True)

    class Meta:
        model = CarouselItem
        fields = ['id', 'nombre', 'imagen', 'url', 'target', 'activo', 'archivos']

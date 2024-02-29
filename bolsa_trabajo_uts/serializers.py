from rest_framework import serializers
from .models import Vacante, Categoria, Descripcion, FormatoReferencia

class FormatoReferenciaSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = Vacante
        fields = '__all__'


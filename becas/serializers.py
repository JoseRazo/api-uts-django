from rest_framework import serializers
from .models import Institucion, Beca, Convocatoria

class ConvocatoriaSerializer(serializers.ModelSerializer):
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
from rest_framework import serializers
from .models import Departamento, Documento
from django.conf import settings

class DocumentoSerializer(serializers.ModelSerializer):
    archivo = serializers.SerializerMethodField()
    categoria_nombre = serializers.SerializerMethodField()  # Agrega este campo para mostrar el nombre de la categoría

    def get_archivo(self, instance):
        request = self.context.get('request')
        if request is not None and instance.archivo:
            archivo_url = request.build_absolute_uri(instance.archivo.url)
            return archivo_url
        return None

    def get_categoria_nombre(self, instance):
        return instance.categoria.nombre  # Devuelve el nombre de la categoría

    class Meta:
        model = Documento
        fields = ['id', 'nombre', 'codigo', 'revision', 'archivo', 'departamento', 'categoria', 'categoria_nombre', 'fecha']

class DepartamentoSerializer(serializers.ModelSerializer):
    documentos = DocumentoSerializer(many=True)

    class Meta:
        model = Departamento
        fields = ['id', 'nombre', 'descripcion', 'documentos']

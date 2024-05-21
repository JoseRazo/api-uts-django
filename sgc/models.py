from django.db import models
from django.contrib.auth.models import User
import os

class Departamento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
def documento_upload_to(instance, filename):
    # Genera la ruta "sgc/documentos/nombre_del_departamento/nombre_de_la_categoria/nombre_del_archivo"
    departamento = instance.departamento.nombre.replace(' ', '_')  # Reemplaza espacios en el nombre del departamento
    categoria = instance.categoria.nombre.replace(' ', '_')  # Reemplaza espacios en el nombre de la categoría
    nombre_archivo, extension = os.path.splitext(filename)
    return f"sgc/documentos/{departamento}/{categoria}/{nombre_archivo}{extension}"

class Documento(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    revision = models.CharField(max_length=2, blank=True, null=True)
    archivo = models.FileField(upload_to=documento_upload_to)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='documentos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='documentos')
    fecha = models.DateField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    creado_por = models.ForeignKey(User, related_name='Creado_por', on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    actualizado_por = models.ForeignKey(User, related_name='Actualizado_por', on_delete=models.SET_NULL, null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        if user:
            if not self.pk:
                # Documento nuevo, establece el usuario como creador
                self.creado_por = user
            else:
                # Documento existente, establece el usuario como actualizador
                self.actualizado_por = user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

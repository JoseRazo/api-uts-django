from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
class Descripcion(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Descripción'
        verbose_name_plural = 'Descripciones'

class FormatoReferencia(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='bolsa_trabajo_uts')
    fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

    class Meta:
        verbose_name = 'Formato Referencia'
        verbose_name_plural = 'Formatos Referencias'

    def __str__(self):
        return self.nombre

class Vacante(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='vacantes')
    descripcion = models.ForeignKey(Descripcion, on_delete=models.CASCADE, related_name='vacantes')
    formato_referencia = models.ForeignKey(FormatoReferencia, on_delete=models.CASCADE, related_name='vacantes')
    convocatoria = models.FileField(upload_to='bolsa_trabajo_uts')
    resultados = models.FileField(null=True, blank=True, upload_to='bolsa_trabajo_uts')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Vacante'
        verbose_name_plural = 'Vacantes'

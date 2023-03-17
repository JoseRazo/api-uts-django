from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.

class Institucion(models.Model):
    nombre = models.CharField(_('Nombre de la institución'), max_length=145)
    url = models.CharField(max_length=145, null=True, blank=True)
    activo = models. BooleanField(default=True)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    
    class Meta:
        verbose_name = 'Institución'
        verbose_name_plural = 'Instituciones'

    def __str__(self):
        return self.nombre
    
class Beca(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='becas')
    nombre = models.CharField(_('Nombre de la beca'), max_length=145)
    descripcion = RichTextField(null=True, blank=True)
    activo = models. BooleanField(default=True)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    
    class Meta:
        verbose_name = 'Beca'
        verbose_name_plural = 'Becas'

    def __str__(self):
        return self.nombre
    
class Convocatoria(models.Model):
    beca = models.ForeignKey(Beca, on_delete=models.CASCADE, related_name='convocatorias')
    nombre = models.CharField(max_length=145)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    archivo_convocatoria = models.FileField(_('Archivo de la convocatoria'), upload_to='becas')
    archivo_resultado = models.FileField(_('Archivo de los resultados'), null=True, blank=True, upload_to='becas')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    
    class Meta:
        verbose_name = 'Convocatoria'
        verbose_name_plural = 'Convocatorias'

    def __str__(self):
        return self.nombre
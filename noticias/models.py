from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=254, unique=True)
    contenido = RichTextField()
    slug = models.SlugField(null=True, unique=True)
    imagen = models.ImageField(upload_to='articulos', verbose_name="Imagen principal")
    fecha_evento = models.DateField(verbose_name='Fecha del evento')
    categoria = models.ForeignKey('Categoria', verbose_name='Categoría', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, verbose_name='Creado por', on_delete=models.CASCADE, editable=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nombre = models.CharField(max_length=254, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class ArticuloImagen(models.Model):
    articulo = models.ForeignKey(Articulo, default=None, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to = 'articulos', null=True, blank=True)

    def __str__(self):
        return self.articulo.titulo

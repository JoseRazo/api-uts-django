from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Instructor(models.Model):
    nombre = models.CharField(max_length=254, unique=True)
    telefono=models.IntegerField(null=True)
    correo=models.EmailField()
    area_estudios=models.TextField(verbose_name='Area de estudios')
    descripcion= RichTextField(verbose_name='Descripción')
    curriculum=models.FileField(blank=True, null=True)
    fecha_creacion= models.DateField(verbose_name='Fecha de creación', auto_now=True)
    fecha_actualizacion=models.DateField(verbose_name='Fecha de actualización', auto_now_add=True)
    fotografia= models.ImageField(upload_to="instructores", blank=True, null=True)

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructores"

    def __str__(self):
        return self.nombre

class Cronograma(models.Model):
    dia= models.DateField()
    hora= models.DateTimeField()
    actividad= models.CharField(max_length=254)
    descripcion= RichTextField()
    fotografia=models.ImageField(upload_to="cronogramas" ,verbose_name='Imagen relacionada', blank=True, null=True)

    class Meta:
        verbose_name = "Cronograma"
        verbose_name_plural = "Cronogramas"

    def __str__(self):
        return self.actividad

class Hotel(models.Model):
    nombre=models.CharField(max_length=254)
    direccion=RichTextField()
    imagen=models.ImageField(upload_to="hoteles", blank=True, null=True)
    url=models.URLField(max_length=254)

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteles"

    def __str__(self):
        return self.nombre
    
class Patrocinadores(models.Model):
    nombre=models.CharField(max_length=254)
    logo=models.ImageField(upload_to="patrocinadores" ,verbose_name="Logo Patrocinador", blank=True, null=True)
    url=models.URLField(max_length=254)

    class Meta:
        verbose_name = "Patrocinador"
        verbose_name_plural = "Patrocinadores"

    def __str__(self):
        return self.nombre

class Header(models.Model):
    seccion=models.CharField(max_length=30)
    url_seccion=models.URLField()

    class Meta:
       verbose_name = "Header"
       verbose_name_plural = "Headers"

    def __str__(self):
        return self.seccion

class Evento(models.Model):
    nombre=models.CharField(max_length=254)
    lugar=models.CharField(max_length=254)
    descripcion=RichTextField()
    mapa=RichTextField()
    logo=models.ImageField(upload_to="eventos", verbose_name="Logo_evento", blank=True, null=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    instructor=models.ForeignKey(Instructor, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=254)
    objetivo=RichTextField()

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self) :
        return self.nombre




from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Instructor(models.Model):
    nombre = models.CharField(max_length=254, unique=True)
    telefono=models.CharField(max_length=15, null=True, blank=True)
    correo=models.EmailField(null=True, blank=True)
    area_estudios=models.CharField(max_length=254, verbose_name='Area de estudios', null=True, blank=True)
    descripcion= RichTextField(verbose_name='Descripción', null=True, blank=True)
    curriculum=models.FileField(blank=True, null=True)
    fecha_creacion= models.DateField(verbose_name='Fecha de creación', auto_now=True)
    fecha_actualizacion=models.DateField(verbose_name='Fecha de actualización', auto_now_add=True)
    fotografia= models.ImageField(upload_to="instructores", blank=True, null=True, default="instructores/perfil-default.png")

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructores"

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=254, unique=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
    
    def __str__(self):
        return self.nombre

    
class Cronograma(models.Model):
    ACTIVIDADES_CHOISES = (
        ('talleres', 'Talleres'),
        ('visitas_industriales', 'Visitas Industriales'),
        ('otro', 'Otro'),
    )
    tipo_actividad = models.CharField(max_length=20, choices=ACTIVIDADES_CHOISES)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    otra_actividad= models.CharField(max_length=254, null=True, blank=True)
    dia = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    fecha= models.DateField()
    hora_inicio= models.TimeField('Hora inicio')
    hora_fin= models.TimeField('Hora fin')

    class Meta:
        verbose_name = "Cronograma"
        verbose_name_plural = "Cronogramas"

    def __str__(self):
        if self.curso:
            return f"Curso: {self.curso}"
        elif self.empresa:
            return f"Empresa: {self.empresa}"
        elif self.otra_actividad:
            return f"Otra Actividad: {self.otra_actividad}"
        else:
            return f"ID: {self.id}"

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
    url_seccion=models.URLField(blank=True, null=True)
    seccion_id= models.CharField(max_length=254, blank=True, null=True)

    class Meta:
       verbose_name = "Header"
       verbose_name_plural = "Headers"

    def __str__(self):
        return self.seccion

class Evento(models.Model):
    nombre=models.CharField(max_length=254)
    lugar=models.CharField(max_length=254)
    descripcion=RichTextField()
    mapa=RichTextField(verbose_name='Mapa')
    logo=models.ImageField(upload_to="eventos", verbose_name="Logo_evento", blank=True, null=True)
    activo = models.BooleanField(default=False)

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
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre





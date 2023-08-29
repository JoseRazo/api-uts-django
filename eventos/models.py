from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.
class Instructor(models.Model):
    nombre = models.CharField(max_length=254, unique=True)
    telefono=models.CharField(max_length=15, null=True, blank=True)
    correo=models.EmailField(null=True, blank=True)
    area_estudios=models.CharField(max_length=254, verbose_name='Area de estudios', null=True, blank=True)
    descripcion= RichTextField(verbose_name='Descripción', null=True, blank=True)
    curriculum=models.FileField(blank=True, null=True)
    fecha_creacion= models.DateField(verbose_name='Fecha de creación', auto_now_add=True)
    fecha_actualizacion=models.DateField(verbose_name='Fecha de actualización', auto_now=True)
    fotografia= models.ImageField(upload_to="instructores", blank=True, null=True, default="perfil-default.png")

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructores"

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=254, unique=True)
    visita_industrial = models.BooleanField(default=False)
    activo = models.BooleanField(default=False)

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
        ordering = ['hora_inicio']

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
    url=models.URLField(max_length=254, null=True, blank=True)

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
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=254)
    objetivo = RichTextField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre



class Registro(models.Model):
    PARTICIPANTE_CHOICES = (
        ('estudiante_utyp', 'Estudiante UTYP'),
        ('docente_directivo_utyp', 'Docente - Directivo UTYP'),
        ('publico_general', 'Público General'),
        ('estudiantes_externos', 'Estudiantes Externos'),
    )

    DIA_CHOICES = (
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
    )
    nombre = models.CharField(max_length=145)
    apellido_paterno = models.CharField(max_length=145, null=True, blank=True)
    apellido_materno = models.CharField(max_length=145, null=True, blank=True)
    email = models.EmailField(max_length=145)
    tipo_participante = models.CharField(max_length=50, choices=PARTICIPANTE_CHOICES)
    universidad_empresa = models.CharField(_('Universidad o Empresa'), max_length=145)
    matricula = models.CharField(max_length=20, null=True, blank=True)
    numero_empleado = models.CharField(max_length=20, null=True, blank=True)
    # foto = models.ImageField(
    #     default='default-640x480.png', upload_to='registro', help_text="El tamaño de la imagen debe ser de 640 x 480 pixeles")
    taller = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    dia_taller = models.CharField(_('Día taller'), max_length=20, choices=DIA_CHOICES, null=True, blank=True)
    visita_industrial = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    dia_visita = models.CharField(_('Día visita industrial'), max_length=20, choices=DIA_CHOICES, null=True, blank=True)
    inscrito = models.BooleanField(default=False)
    referencia = models.CharField(max_length=140, null=True, blank=True)
    comprobante_pago = models.FileField(upload_to='registro/comprobante', null=True, blank=True)
    formato_inscripcion = models.FileField(upload_to='registro/inscripcion', null=True, blank=True)
    fecha_creacion= models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    fecha_actualizacion=models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return f'{self.nombre}'
    
    def nombre_completo(self):
        campos_nombre = [self.nombre]
        if self.apellido_paterno:
            campos_nombre.append(self.apellido_paterno)
        if self.apellido_materno:
            campos_nombre.append(self.apellido_materno)
        return ' '.join(campos_nombre)


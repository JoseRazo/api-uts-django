from django.db import models

# Create your models here.

class Carousel(models.Model):
    nombre = models.CharField(max_length=254, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
      verbose_name = "Carousel"
      verbose_name_plural = "Carousels"
      ordering = ['fecha_creacion']

    def __str__(self):
        return self.nombre
      
class CarouselItem(models.Model):
    TARGET_CHOICES = (
        ('_blank', 'Nueva pestaña'),
        ('_self', 'Misma pestaña'),
    )
    nombre = models.CharField(max_length=254)
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE, related_name='carousel_items')
    imagen = models.ImageField(upload_to="carousel/imagenes", blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    target = models.CharField(max_length=10, choices=TARGET_CHOICES, default='_self')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
      verbose_name = "Carousel Item"
      verbose_name_plural = "Carousel Items"
      ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre
      
class CarouselItemFile(models.Model):
    item = models.ForeignKey(CarouselItem, on_delete=models.CASCADE, related_name='archivos')
    nombre = models.CharField(max_length=254)
    archivo = models.FileField(upload_to="carousel/archivos")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Archivo del Item"
        verbose_name_plural = "Archivos del Item"

    def __str__(self):
        return f"{self.nombre} ({self.item.nombre})"
      
      
      
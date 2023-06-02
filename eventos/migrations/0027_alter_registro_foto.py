# Generated by Django 3.2 on 2023-06-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0026_alter_registro_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='foto',
            field=models.ImageField(blank=True, default='default-640x480.png', help_text='El tamaño de la imagen debe ser de 640 x 480 pixeles', null=True, upload_to='registro'),
        ),
    ]

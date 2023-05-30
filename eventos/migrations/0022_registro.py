# Generated by Django 3.2 on 2023-05-30 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0021_remove_cronograma_fotografia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=145)),
                ('apellido_paterno', models.TextField(max_length=145)),
                ('apellido_materno', models.TextField(max_length=145)),
                ('escuela_procedencia', models.TextField(max_length=145)),
                ('foto', models.ImageField(default='default-640x480.png', help_text='El tamaño de la imagen debe ser de 540 x 540 pixeles', upload_to='registro')),
                ('inscrito', models.BooleanField(default=False)),
                ('referencia', models.TextField(max_length=140)),
                ('comprobante_pago', models.FileField(upload_to='registro/comprobante')),
                ('taller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.curso')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
    ]

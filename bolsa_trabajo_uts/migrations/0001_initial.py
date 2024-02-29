# Generated by Django 3.2 on 2024-02-29 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Descripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vacante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('convocatoria', models.FileField(upload_to='bolsa_trabajo_uts')),
                ('resultados', models.FileField(blank=True, null=True, upload_to='bolsa_trabajo_uts')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacantes', to='bolsa_trabajo_uts.categoria')),
                ('descripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacantes', to='bolsa_trabajo_uts.descripcion')),
            ],
        ),
    ]

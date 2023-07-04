# Generated by Django 3.2 on 2023-06-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0023_auto_20230621_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='matricula',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='numero_empleado',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

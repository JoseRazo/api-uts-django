# Generated by Django 3.2 on 2023-08-29 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0028_auto_20230704_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='activo',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]

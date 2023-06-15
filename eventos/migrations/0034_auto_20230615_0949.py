# Generated by Django 3.2 on 2023-06-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0033_registro_taller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='apellido_materno',
            field=models.CharField(max_length=145),
        ),
        migrations.AlterField(
            model_name='registro',
            name='apellido_paterno',
            field=models.CharField(max_length=145),
        ),
        migrations.AlterField(
            model_name='registro',
            name='escuela_procedencia',
            field=models.CharField(max_length=145),
        ),
        migrations.AlterField(
            model_name='registro',
            name='nombre',
            field=models.CharField(max_length=145),
        ),
        migrations.AlterField(
            model_name='registro',
            name='referencia',
            field=models.CharField(max_length=140, unique=True),
        ),
    ]
# Generated by Django 3.2 on 2023-06-02 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0027_alter_registro_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='referencia',
            field=models.TextField(max_length=140, unique=True),
        ),
    ]

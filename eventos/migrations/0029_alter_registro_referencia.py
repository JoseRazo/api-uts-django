# Generated by Django 3.2 on 2023-06-02 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0028_alter_registro_referencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='referencia',
            field=models.TextField(max_length=140),
        ),
    ]
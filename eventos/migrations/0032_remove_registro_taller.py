# Generated by Django 3.2 on 2023-06-12 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0031_auto_20230612_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='taller',
        ),
    ]

# Generated by Django 3.2 on 2023-05-19 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0020_auto_20230519_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cronograma',
            name='fotografia',
        ),
    ]

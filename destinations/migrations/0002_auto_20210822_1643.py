# Generated by Django 2.2 on 2021-08-22 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='prueba',
        ),
        migrations.DeleteModel(
            name='Prueba',
        ),
    ]
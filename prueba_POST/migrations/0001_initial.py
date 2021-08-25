# Generated by Django 2.2 on 2021-08-22 22:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adultos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adultos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='bebes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bebes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='confort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confort', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='conGuia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conGuia', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='destinationFromSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinationFromSearch', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='doble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doble', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='duracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duracion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='estandar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estandar', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='excursiones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excursiones', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='lujo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lujo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='mediaPension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediaPension', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='niños',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='pensionCompleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='presupuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='regular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='selectedDateEnd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='selectedDateStart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='shows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='single',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='sinGuia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='soloDesayuno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='traslados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='triple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
    ]
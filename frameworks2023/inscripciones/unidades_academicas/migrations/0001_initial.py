# Generated by Django 4.1.4 on 2023-02-21 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('direccion', models.CharField(default='sin dirección', max_length=350, verbose_name='Dirección')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramaAcademico',
            fields=[
                ('clave', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono')),
                ('unidad_academica', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='unidades_academicas.unidadacademica', verbose_name='Unidad Académica')),
            ],
        ),
    ]

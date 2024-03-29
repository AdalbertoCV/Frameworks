# Generated by Django 4.1.4 on 2023-03-23 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_estado_municipio'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.estado', verbose_name='Estado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='municipio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.municipio', verbose_name='Municipio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docente',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.estado', verbose_name='Estado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docente',
            name='municipio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.municipio', verbose_name='Municipio'),
            preserve_default=False,
        ),
    ]

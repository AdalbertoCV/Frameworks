from django.db import models
from django.contrib.auth.models import User

class Docente(models.Model):
    matricula = models.CharField('Matricula', max_length=50)
    rfc = models.CharField('R.F.C', max_length=13)
    apellido_paterno = models.CharField(max_length=150)
    avatar = models.ImageField('Foto de perfil', upload_to = 'perfiles')
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete= models.CASCADE)
    fecha_nacimiento = models.DateField()

class Alumno(models.Model):
    matricula = models.CharField('Matricula', max_length=50)
    apellido_paterno = models.CharField(max_length=150)
    avatar = models.ImageField('Foto de perfil', upload_to = 'perfiles')
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete= models.CASCADE)
    fecha_nacimiento = models.DateField()
    programa = models.ForeignKey("unidades_academicas.ProgramaAcademico", verbose_name= "Programa", on_delete= models.CASCADE)
from django.db import models
from django.contrib.auth.models import User

class Docente(models.Model):
    matricula = models.CharField('Matricula', max_length=50)
    rfc = models.CharField('R.F.C', max_length=13)
    apellido_paterno = models.CharField(max_length=150)
    avatar = models.ImageField('Foto de perfil', upload_to = 'perfiles', null=True, blank=True)
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete= models.CASCADE)
    fecha_nacimiento = models.DateField()
    estado = models.ForeignKey("usuarios.Estado", verbose_name= "Estado", on_delete= models.DO_NOTHING )
    municipio = models.ForeignKey("usuarios.Municipio", verbose_name= "Municipio", on_delete= models.DO_NOTHING )

class Alumno(models.Model):
    matricula = models.CharField('Matricula', max_length=50)
    apellido_paterno = models.CharField(max_length=150)
    avatar = models.ImageField('Foto de perfil', upload_to = 'perfiles',null=True, blank=True)
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete= models.CASCADE)
    fecha_nacimiento = models.DateField()
    programa = models.ForeignKey("unidades_academicas.ProgramaAcademico", verbose_name= "Programa", on_delete= models.CASCADE)
    estado = models.ForeignKey("usuarios.Estado", verbose_name= "Estado", on_delete= models.DO_NOTHING )
    municipio = models.ForeignKey("usuarios.Municipio", verbose_name= "Municipio", on_delete= models.DO_NOTHING )

class Estado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return  self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.ForeignKey("usuarios.Estado", verbose_name = "Estado", on_delete= models.DO_NOTHING)

    def __str__(self):
        return  self.nombre
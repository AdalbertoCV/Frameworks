from django.db import models

class Docente(models.Model):
    matricula = models.CharField('matricula', primary_key= True, max_length=10)
    nombre = models.CharField('nombre', max_length=50)
    apellidoPaterno = models.CharField('apellidopaterno', max_length=50)
    apellidoMaterno = models.CharField('apellidomaterno', max_length=50)
    def __str__(self):
        return self.nombre + " " + self.apellidoPaterno + " " + self.apellidoMaterno

class Hora(models.Model):
    clave = models.IntegerField('clave', primary_key=True)
    horaInicio = models.CharField('horainicio', max_length=5)
    horaFin = models.CharField('horafin', max_length=5)
    def __str__(self):
        return self.horaInicio +"-"+ self.horaFin

class Salon(models.Model):
    clave = models.IntegerField('clave', primary_key=True)
    nombre = models.CharField('nombre', max_length=50)
    def __str__(self):
        return self.nombre 

SEMESTRE = [
('','-------------'),
('1','1er Semestre'),
('2','2do Semestre'),
('3','3er Semestre'),
('4','4to Semestre'),
('5','5to Semestre'),
('6','6to Semestre'),
('7','7mo Semestre'),
('8','8vo Semestre'),
('9','9no Semestre')]

DIA = [
    ('','-------------'),
    ('1','Lunes'),
    ('2','Martes'),
    ('3','Miércoles'),
    ('4','Jueves'),
    ('5','Viernes'),
    ('6','Sábado'),
]
class Horario(models.Model):
    clave = models.IntegerField('Clave', primary_key=True, default=0)
    materia = models.ForeignKey('materias.Materia',verbose_name = "Materia", on_delete=models.CASCADE)
    docente = models.ForeignKey('Docente',verbose_name = "Docente", on_delete=models.CASCADE)
    semestre = models.CharField(max_length=2, choices = SEMESTRE)
    dia = models.CharField(max_length=2, choices = DIA)
    hora = models.ForeignKey('Hora',verbose_name = "Hora", on_delete=models.CASCADE)
    salon = models.ForeignKey('Salon',verbose_name = "Salon", on_delete=models.CASCADE)



from django.db import models

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
class Materia(models.Model):
    clave = models.CharField(primary_key = True , max_length=10)
    nombre = models.CharField(max_length=100)
    creditos = models.SmallIntegerField('Créditos')
    semestre = models.CharField(max_length=2, choices = SEMESTRE)
    optativa = models.BooleanField(default=False)
    programa = models.ForeignKey("unidades_academicas.ProgramaAcademico", verbose_name="Programa Academico", on_delete= models.DO_NOTHING)

    def __str__(self):
        return f"{self.nombre} - {self.clave}" 

class MateriasPrecedentes(models.Model):
    materia = models.ForeignKey("Materia", verbose_name = "Materia", on_delete=models.CASCADE, related_name='materia_actual')
    materia_precedente = models.ForeignKey("Materia", verbose_name = "Materia Precedente", on_delete=models.CASCADE, related_name='materia_precedente')

    def __str__(self):
        return f"{self.materia} - {self.materia_precedente}" 
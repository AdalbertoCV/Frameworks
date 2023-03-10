from django import forms
from .models import Horario

class FormHorario(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'

        widgets = {
            'clave': forms.NumberInput(attrs= {'class': 'form-control', 'placeholder': 'Clave'}),
            'materia': forms.Select(attrs= {'class':'form-control','placeholder':'Materia'}),
            'docente': forms.Select(attrs= {'class':'form-control','placeholder':'Docente'}),
            'semestre': forms.Select(attrs= {'class':'form-control','placeholder':'Semestre'}),
            'dia': forms.Select(attrs= {'class':'form-control','placeholder':'Dia'}),
            'hora': forms.Select(attrs= {'class':'form-control','placeholder':'Hora'}),
            'salon': forms.Select(attrs= {'class':'form-control','placeholder':'Salón'})
            }

class FormHorarioEditar(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['clave']

        widgets = {
            #'clave': forms.NumberInput(attrs= {'class': 'form-control', 'placeholder': 'Clave'}),
            'materia': forms.Select(attrs= {'class':'form-control','placeholder':'Materia'}),
            'docente': forms.Select(attrs= {'class':'form-control','placeholder':'Docente'}),
            'semestre': forms.Select(attrs= {'class':'form-control','placeholder':'Semestre'}),
            'dia': forms.Select(attrs= {'class':'form-control','placeholder':'Dia'}),
            'hora': forms.Select(attrs= {'class':'form-control','placeholder':'Hora'}),
            'salon': forms.Select(attrs= {'class':'form-control','placeholder':'Salón'})
            }
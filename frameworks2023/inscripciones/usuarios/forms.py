from django import forms
from .models import Docente, Alumno

class FormDocente(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

class FormAlumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
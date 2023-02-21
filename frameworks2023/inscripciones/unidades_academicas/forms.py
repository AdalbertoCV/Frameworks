from django import forms
from unidades_academicas.models import ProgramaAcademico

class FormPrograma(forms.ModelForm):
    class Meta:
        model = ProgramaAcademico
        fields = '__all__'
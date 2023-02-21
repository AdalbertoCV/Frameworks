from django import forms
from unidades_academicas.models import ProgramaAcademico, UnidadAcademica

class FormPrograma(forms.ModelForm):
    class Meta:
        model = ProgramaAcademico
        fields = '__all__'

class FormUnidad(forms.ModelForm):
    class Meta:
        model = UnidadAcademica
        fields = '__all__'
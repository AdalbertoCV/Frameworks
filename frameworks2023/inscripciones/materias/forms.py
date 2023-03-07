from django import forms
from .models import Materia

class FormMateria(forms.ModelForm):
    class Meta:
        model = Materia
        #exclude = ['nombre']
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs= {'class':'form-control','placeholder':'Nombre'}),
            'clave': forms.TextInput(attrs= {'class':'form-control','placeholder':'Clave Materia'}),
            'semestre': forms.Select(attrs= {'class':'form-control','placeholder':'Semestre'}),
            #'optativa': forms.TextInput(attrs= {'class':'form-control','placeholder':'Optativa'}),
            'creditos': forms.NumberInput(attrs= {'class':'form-control','placeholder':'No. Creditos'})
            }

class FormMateriaEditar(forms.ModelForm):
    class Meta:
        model = Materia
        exclude = ['clave']

        widgets = {
            'nombre': forms.TextInput(attrs= {'class':'form-control','placeholder':'Nombre'}),
            #'clave': forms.TextInput(attrs= {'class':'form-control','placeholder':'Clave Materia'}),
            'semestre': forms.Select(attrs= {'class':'form-control','placeholder':'Semestre'}),
            #'optativa': forms.TextInput(attrs= {'class':'form-control','placeholder':'Optativa'}),
            'creditos': forms.NumberInput(attrs= {'class':'form-control','placeholder':'No. Creditos'})
            }
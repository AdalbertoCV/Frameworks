from django import forms
from .models import Materia, SEMESTRE

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

class FiltrosMateria(FormMateria):
    def __init__(self, *args, **kwargs):
        super(FiltrosMateria, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False

# class FiltrosMateria(forms.Form):
#     nombre = forms.CharField(
#         widget= forms.TextInput(attrs={'placeholder':'Nombre','class': 'form-control'}),
#         required = False,
#         )
#     clave = forms.CharField(
#         widget= forms.TextInput(attrs={'placeholder':'Clave','class': 'form-control'}),
#         required = False,
#         )
#     semestre = forms.CharField(
#         widget= forms.Select(choices = SEMESTRE ,attrs={'placeholder':'Semestre','class': 'form-control'}),
#         required = False,
#         )
#     creditos = forms.CharField(
#         widget= forms.NumberInput(attrs={'placeholder':'Creditos','class': 'form-control'}),
#         required = False,
#         )
#     optativa = forms.CharField(
#         widget= forms.CheckboxInput(),
#         required = False,
#         )

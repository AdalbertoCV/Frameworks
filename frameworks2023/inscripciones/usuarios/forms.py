from django import forms
from .models import Docente, Alumno
from django.urls import reverse_lazy

class FormDocente(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

        widgets = {
            'estado': forms.Select(attrs={'class':'form-control', 'data-url': reverse_lazy('buscaMunicipios')})
        }

        def __init__(self, *args, **kwargs):
            super(FormDocente, self).__init__(*args, **kwargs)
            self.fields['avatar'].required = False
        


class FormAlumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(FormAlumno, self).__init__(*args, **kwargs)
            self.fields['avatar'].required = False
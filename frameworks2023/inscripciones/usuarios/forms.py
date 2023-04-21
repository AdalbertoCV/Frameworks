from django import forms
from .models import Docente, Alumno
from django.urls import reverse_lazy
from django.contrib.auth.models import User

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

class UserForm(forms.ModelForm):
    re_pass = forms.CharField(label='Confirm Password', widget = forms.PasswordInput(), required= True)
    password = forms.CharField(label='Password', widget = forms.PasswordInput(), required= True)
    class Meta:
        model = User
        fields = ['username','password','email']
    def clean_password(self, *args, **kargs):
        if self.data['password'] != self.data['re_pass']:
            raise forms.ValidationError('Password dont match', code = 'passwords_not_equals')
        return self.data['password']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class FormPerfilDocente(forms.ModelForm):
    class Meta:
        model = Docente
        exclude = ['usuario']
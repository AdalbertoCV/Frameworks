from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from .models import Docente,Alumno, Estado, Municipio
from .forms import FormDocente,FormAlumno
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse

#def login(request):
 #   return render(request, 'login.html')

class RegistrarDocente(SuccessMessageMixin,CreateView):
    model = Docente
    template_name = 'registrar.html'
    form_class = FormDocente
    success_message = '%(username)s se registro con éxito'
    success_url = reverse_lazy('login')

class RegistrarAlumno(SuccessMessageMixin,CreateView):
    model = Alumno
    template_name = 'registrar.html'
    form_class = FormAlumno
    success_message = '%(username)s se registro con éxito'
    success_url = reverse_lazy('login')

class LoginView(LoginView):
    template_name = 'Login.html'
    form_class = AuthenticationForm


def busca_municipios(request):
    id_estado = request.POST.get('id_estado', None)
    if id_estado:
        municipios = Municipio.objects.filter(estado_id = id_estado)
        data = [{'id':mun.id, 'nombre':mun.nombre} for mun in municipios]
        return JsonResponse(data, safe = False)
    return JsonResponse({'error':'Parámetro inválido'}, safe=False)
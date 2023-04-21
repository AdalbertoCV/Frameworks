from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from .models import Docente,Alumno, Estado, Municipio
from .forms import FormDocente,FormAlumno, UserForm, FormPerfilDocente
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.contrib.auth.models import User
#def login(request):
 #   return render(request, 'login.html')
 
def perfil(request):
    #print(request.user.docente)
    try:
        docente = request.user.docente
    except:
        docente = None
    if request.method == 'POST':
        if docente:
            form = FormPerfilDocente(request.POST, request.FILES,instance= docente)
        else:
            form = FormPerfilDocente(request.POST, request.FILES)
        if form.is_valid():
            docente = form.save(commit=False)
            docente.usuario = request.user
            docente.save()
            return redirect('home')
    else:
        if docente:
            form = FormPerfilDocente(instance= docente)
        else:
            form = FormPerfilDocente()
    return render(request, 'perfil_docente.html', {'form':form})


class RegistrarDocente(SuccessMessageMixin,CreateView):
    model = Docente
    template_name = 'registrar.html'
    form_class = FormDocente
    success_message = '%(username)s se registro con éxito'
    success_url = reverse_lazy('login')

class RegistrarDocente2(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'registrar_docente2.html'
    form_class = UserForm
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
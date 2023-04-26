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
from .token import token_activacion
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.views.generic import TemplateView
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
    def form_valid(self, form):
        form = UserForm(self.request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # miapp.com
            # localhost:8000
            dominio = get_current_site(self.request)
            mensaje = render_to_string('confirmar_cuenta.html',
                {
                    'user':user,
                    'dominio':dominio,
                    'uid': urlsafe_base64_encode(force_bytes(user.id)),
                    'token': token_activacion.make_token(user)
                }
            )

            email = EmailMessage(
                'Activar cuenta ',
                mensaje,
                to=[user.email]
            )
            email.content_subtype = "html"
            email.send()
        else:
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)

class ActivarCuenta(TemplateView):
    def get(self, request, *args, **kwargs):
        # context = self.get_context_data(**kwargs)

        try:
            uid = urlsafe_base64_decode(kwargs['uidb64'])
            token = kwargs['token']
            user = User.objects.get(pk=uid) 
        except(TypeError, ValueError, User.DoesNotExist):
            user = None
        
        if user is not None and token_activacion.check_token(user, token):
            user.is_active = True
            user.save()
            mensaje = 'Cuenta activada, ingresar datos'
        else:
            mensaje = 'Token inválido, contacta al administrador'

        return render(request, 'login.html',{'mensaje':mensaje})
        
        # return self.render_to_response(context)

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
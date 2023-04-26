from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Materia
from .forms import FormMateria, FormMateriaEditar, FiltrosMateria
from unidades_academicas.models import ProgramaAcademico
from django.core.paginator import Paginator

class ListaMaterias(ListView):
    paginate_by = 5
    model = Materia
    extra_context = {'form': FiltrosMateria}

def eliminar_materias(request):
    pass

class NuevaMateria(CreateView):
    model = Materia
    extra_context = {'accion': 'Agregar'}
    #fields = '__all__'
    form_class = FormMateria
    success_url = reverse_lazy('lista_materias')

class EditarMateria(UpdateView):
    model = Materia
    form_class = FormMateriaEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_materias')

class EliminarMateria(DeleteView):
    model= Materia
    success_url = reverse_lazy('lista_materias')

class Bienvenida(TemplateView):
    template_name = 'home.html'

class Bienvenida2(TemplateView):
    template_name = 'home2.html'

def BuscarMateria(request):
    materias = Materia.objects.all().order_by('nombre','semestre')
    form = FiltrosMateria(request.POST)
    if request.method == 'POST':
        clave = request.POST.get('clave',None)
        nombre = request.POST.get('nombre',None)
        semestre = request.POST.get('semestre',None)
        creditos = request.POST.get('creditos',None)
        optativa = request.POST.get('optativa',None)
        programa = request.POST.get('programa',None)
        programa2 = request.POST.get('Programa2',None)
        #programa = ProgramaAcademico.objects.get(clave=programa)

        if clave:
            materias = materias.filter(clave= clave)
        if nombre:
            materias = materias.filter(nombre__icontains = nombre)
        if semestre:
            materias = materias.filter(semestre= semestre)
        if creditos:
            materias = materias.filter(creditos= creditos)
        if optativa == '1':
            materias = materias.filter(optativa= True)
        elif optativa=='2':
            materias = materias.filter(optativa= False)
        if programa:
            materias = materias.filter(programa__clave= programa)
        if programa2:
            materias = materias.filter(programa__nombre__contains= programa2)
        #else:
        #    materias = materias.filter(optativa= False)
    #print(materias.query)
    paginator = Paginator(materias,5)
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'object_list': page_obj, 'page_obj': page_obj, 'form': form}
    return render(request, 'materias/materia_list.html', context)
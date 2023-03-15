from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Materia
from .forms import FormMateria, FormMateriaEditar, FiltrosMateria
from unidades_academicas.models import ProgramaAcademico

class ListaMaterias(ListView):
    model = Materia
    extra_context = {'form': FiltrosMateria}

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
        programa = ProgramaAcademico.objects.get(clave=programa)

        if clave:
            materias = materias.filter(clave= clave)
        if nombre:
            materias = materias.filter(nombre__icontains = nombre)
        if semestre:
            materias = materias.filter(semestre= semestre)
        if creditos:
            materias = materias.filter(creditos= creditos)
        if optativa == 'on':
            materias = materias.filter(optativa= True)
        if programa:
            materias = materias.filter(programa= programa)
        #else:
        #    materias = materias.filter(optativa= False)
    print(materias.query)
    context = {'object_list': materias, 'form': form}
    return render(request, 'materias/materia_list.html', context)
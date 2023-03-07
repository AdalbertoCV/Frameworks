from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Materia
from .forms import FormMateria, FormMateriaEditar

class ListaMaterias(ListView):
    model = Materia

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
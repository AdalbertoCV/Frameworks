from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Horario
from .forms import FormHorario, FormHorarioEditar
from django.core.paginator import Paginator

class ListaHorarios(ListView):
    model = Horario
    paginate_by = 5

class NuevoHorario(CreateView):
    model = Horario
    extra_context = {'accion': 'Agregar'}
    form_class = FormHorario
    success_url = reverse_lazy('lista_horarios')

class EditarHorario(UpdateView):
    model = Horario
    form_class = FormHorarioEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_horarios')

class EliminarHorario(DeleteView):
    model= Horario
    success_url = reverse_lazy('lista_horarios')
from django.shortcuts import render
from django.views.generic import ListView
from .models import Materia

class ListaMaterias(ListView):
    model = Materia


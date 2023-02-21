from django.shortcuts import render, redirect
from unidades_academicas.models import ProgramaAcademico
from unidades_academicas.forms import FormPrograma

def lista_programas(request):
    contexto = {'Programas':ProgramaAcademico.objects.all()}
    return render(request, 'lista_programas.html', contexto)

def agregar_programa(request):
    if request.method == 'POST':
        form = FormPrograma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_programas')
    else:
        form = FormPrograma()
    contexto = {'form': form}
    return render(request, 'agregar_programas.html', contexto)

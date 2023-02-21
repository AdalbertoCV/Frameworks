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

def eliminar_programa(request, clave):
    ProgramaAcademico.objects.get(clave = clave).delete()
    return redirect('lista_programas')

def editar_programa(request, clave):
    programa = ProgramaAcademico.objects.get(clave = clave)
    if request.method == 'POST':
        form = FormPrograma(request.POST, instance = programa)
        if form.is_valid():
            form.save()
            return redirect('lista_programas')
    else:
        form = FormPrograma(instance = programa)
    contexto = {'form': form}
    return render(request, 'editar_programa.html', contexto)
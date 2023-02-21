from django.shortcuts import render, redirect
from unidades_academicas.models import ProgramaAcademico, UnidadAcademica
from unidades_academicas.forms import FormPrograma, FormUnidad

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


def lista_unidades(request):
    contexto = {'Unidades':UnidadAcademica.objects.all()}
    return render(request, 'lista_unidades.html', contexto)

def agregar_unidad(request):
    if request.method == 'POST':
        form = FormUnidad(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_unidades')
    else:
        form = FormUnidad()
    contexto = {'form': form}
    return render(request, 'agregar_unidad.html', contexto)

def eliminar_unidad(request, nombre):
    UnidadAcademica.objects.get(nombre = nombre).delete()
    return redirect('lista_unidades')

def editar_unidad(request, nombre):
    unidad = UnidadAcademica.objects.get(nombre = nombre)
    if request.method == 'POST':
        form = FormUnidad(request.POST, instance = unidad)
        if form.is_valid():
            form.save()
            return redirect('lista_unidades')
    else:
        form = FormUnidad(instance = unidad)
    contexto = {'form': form}
    return render(request, 'editar_unidad.html', contexto)
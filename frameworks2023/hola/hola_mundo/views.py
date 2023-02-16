from django.shortcuts import render

def hola(request):
    return render(request, 'hola.html')

def saludo(request, id):
    materias = [
        'Linux',
        'Álgebra',
        'Administración de proyectos de software',
        'Pruebas y mantenimiento de software',
        'Deployment'
    ]
    calificaciones = [
        {'mat':'Linux','cal': 9},
        {'mat':'Álgebra','cal': 8},
        {'mat':'Administración de proyectos de software','cal': 7},
        {'mat':'Pruebas y mantenimiento de software', 'cal':10},
        {'mat':'Deployment','cal': 5},
    ]
    otro_id = id if id else 0
    
    # if id:
    #     otro_id = id
    # else:
    #     otro_id = 0
    
    context = {
        'nombre':'Adal',
        'edad':20,
        'materias':materias,
        'calificaciones':calificaciones,
        'id': otro_id
    }
    
    return render(request, 'saludo.html', context)

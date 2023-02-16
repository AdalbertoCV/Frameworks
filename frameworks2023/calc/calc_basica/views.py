from django.shortcuts import render

def calculadora(request):
    return render (request, 'calc_basica.html')

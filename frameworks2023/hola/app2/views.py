from django.shortcuts import render

def mensaje(request):
    return render(request,'mensaje_app2.html')

def  hola(request):
    return render(request,'hola_app2.html')
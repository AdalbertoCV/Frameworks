from django.shortcuts import render

def calculadora(request):
    res = ''
    if request.method == 'POST':
        n1 = request.POST.get('n1', None)
        n2 = request.POST.get('n2', None)
        if (n1 and n2):
            res = "La suma es: " + str((int(n1) + int(n2)))
    return render(request,'calc.html',{'suma':res})

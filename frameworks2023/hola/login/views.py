from django.shortcuts import render

def login(request):
    mensaje = None
    if request.method == 'POST':
        username = request.POST.get('uname', None)
        password = request.POST.get('psw', None)
        mensaje = 'Usuario invalido'
        if username == 'Adal' and password == 'admin1234':
            return render(request, 'loged.html')
        else:
            return render(request, 'login.html', {'mensaje': mensaje})
    else:
        return render(request, 'login.html', {'mensaje': mensaje})
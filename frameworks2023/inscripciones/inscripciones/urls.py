from django.contrib import admin
from django.urls import path, include
from materias.views import Bienvenida, Bienvenida2
from usuarios.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('admin/',admin.site.urls),
    path('programas/', include('unidades_academicas.urls_programas')),
    path('unidades/', include('unidades_academicas.urls_unidades')),
    path('materias/', include('materias.urls')),
    path('horarios/', include('horarios.urls')),
    path('home/', Bienvenida.as_view(), name = 'home'),
    path('dashboard/', Bienvenida2.as_view(), name = 'home2'),
    path('usuarios/', include('usuarios.urls'))
]

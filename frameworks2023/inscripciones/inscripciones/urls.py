from django.contrib import admin
from django.urls import path, include
from materias.views import Bienvenida, Bienvenida2

urlpatterns = [
    path('admin/',admin.site.urls),
    path('programas/', include('unidades_academicas.urls_programas')),
    path('unidades/', include('unidades_academicas.urls_unidades')),
    path('materias/', include('materias.urls')),
    path('horarios/', include('horarios.urls')),
    path('', Bienvenida.as_view(), name = 'home'),
    path('dashboard/', Bienvenida2.as_view(), name = 'home2'),
    path('usuarios/', include('usuarios.urls'))
]

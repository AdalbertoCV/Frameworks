from django.contrib import admin
from django.urls import path, include
from materias.views import Bienvenida

urlpatterns = [
    path('admin/',admin.site.urls),
    path('programas/', include('unidades_academicas.urls_programas')),
    path('unidades/', include('unidades_academicas.urls_unidades')),
    path('materias/', include('materias.urls')),
    path('horarios/', include('horarios.urls')),
    path('', Bienvenida.as_view(), name = 'home'),
]

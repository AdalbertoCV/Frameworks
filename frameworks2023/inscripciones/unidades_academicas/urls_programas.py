from django.urls import path
from unidades_academicas import views

urlpatterns = [
    path('', views.lista_programas, name='lista_programas'),
    path('agregar/', views.agregar_programa, name='agregar_programa'),
    path('eliminar/<int:clave>', views.eliminar_programa, name= 'eliminar_programa'),
    path('editar/<int:clave>', views.editar_programa, name= 'editar_programa'),
]
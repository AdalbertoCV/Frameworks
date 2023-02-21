from django.urls import path
from unidades_academicas import views

urlpatterns = [
    path('', views.lista_programas, name='lista_programas'),
    path('Agregar/', views.agregar_programa, name='agregar_programa'),
]
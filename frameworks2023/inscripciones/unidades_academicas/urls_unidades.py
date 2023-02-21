from django.urls import path
from unidades_academicas import views

urlpatterns = [
    path('', views.lista_unidades, name='lista_unidades'),
    path('agregar/', views.agregar_unidad, name='agregar_unidad'),
    path('eliminar/<str:nombre>', views.eliminar_unidad, name= 'eliminar_unidad'),
    path('editar/<str:nombre>', views.editar_unidad, name= 'editar_unidad'),
]
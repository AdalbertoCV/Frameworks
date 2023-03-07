from django.urls import path, include
from materias import views

urlpatterns = [
    path('', views.ListaMaterias.as_view(), name = 'lista_materias'),
    path('agregar/', views.NuevaMateria.as_view(), name = 'agregar_materia'),
    path('editar/<str:pk>', views.EditarMateria.as_view(), name = 'editar_materia'),
    path('eliminar/<str:pk>', views.EliminarMateria.as_view(), name = 'eliminar_materia'),
]

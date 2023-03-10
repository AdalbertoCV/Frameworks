from django.urls import path, include
from horarios import views

urlpatterns = [
    path('', views.ListaHorarios.as_view(), name = 'lista_horarios'),
    path('agregar/', views.NuevoHorario.as_view(), name = 'agregar_horario'),
    path('editar/<int:pk>', views.EditarHorario.as_view(), name = 'editar_horario'),
    path('eliminar/<int:pk>', views.EliminarHorario.as_view(), name = 'eliminar_horario'),
]

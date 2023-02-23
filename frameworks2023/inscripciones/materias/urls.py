from django.urls import path, include
from materias import views

urlpatterns = [
    path('', views.ListaMaterias.as_view(), name = 'lista_materias'),
]

from django.urls import path
from hola_mundo import views

urlpatterns = [
    path('hola/', views.hola),
    path('saludo/', views.saludo),
    path('saludo/<int:id>', views.saludo),
]

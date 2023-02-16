from django.urls import path
from app2 import views

urlpatterns = [
    path('mensaje/', views.mensaje),
    path('hola/', views.hola),
]

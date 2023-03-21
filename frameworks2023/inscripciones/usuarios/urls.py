from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registrar-docente/', views.RegistrarDocente.as_view(), name='registrarDocente'),
    path('registrar-alumno/', views.RegistrarAlumno.as_view(), name='registrarAlumno'),
]
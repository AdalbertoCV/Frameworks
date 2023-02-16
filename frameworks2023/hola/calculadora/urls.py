from django.urls import path
from calculadora import views

urlpatterns = [
    path('', views.calculadora),
]

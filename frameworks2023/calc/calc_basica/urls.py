from django.urls import path
from calc_basica import views

urlpatterns = [
    path('calculadora/', views.calculadora),
]

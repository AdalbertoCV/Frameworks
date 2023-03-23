from django.contrib import admin
from .models import Docente,Alumno, Estado, Municipio

admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(Estado)
admin.site.register(Municipio)
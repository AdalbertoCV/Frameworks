from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hola_mundo.urls')),
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
    path('login/', include('login.urls')),
    path('calculadora/', include('calculadora.urls')),
]

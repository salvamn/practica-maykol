"""
URL configuration for practica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views


urlpatterns = [
    path('inicio', views.inicio_admin, name='inicio_admin'),
    path('instituciones/<str:institucion>/<str:tipo_equipo>', views.instituciones_admin, name='instituciones_admin'), # https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#url
    # Lebu
    path('obtener_grafico_lebu/', views.obtener_grafico_institucion_lebu, name='obtener_grafico_lebu'),
    path('obtener_data_equipos_medicos_lebu/', views.obtener_data_equipos_medicos_lebu, name='obtener_data_equipos_medicos_lebu'),
    path('obtener_data_ambulancias_lebu/', views.obtener_data_ambulancias_lebu, name='obtener_data_ambulancias_lebu'),
    path('obtener_data_general_lebu/', views.obtener_data_total_lebu, name='obtener_data_general_lebu'),
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    # Arauco
    path('obtener_data_total_arauco/', views.obtener_data_total_institucion_arauco, name='obtener_data_total_arauco'),
    path('obtener_data_equipos_medicos_arauco/', views.obtener_data_equipos_medicos_arauco, name='obtener_data_equipos_medicos_arauco'),
    path('obtener_data_equipos_industriales_arauco/', views.obtener_data_equipos_industriales_arauco, name='obtener_data_equipos_industriales_arauco'),
    path('obtener_data_vehiculos_arauco/', views.obtener_data_vehiculos_arauco, name='obtener_data_vehiculos_arauco'),
    # Cañete
    path('obtener_data_total_institucion_canete/', views.obtener_data_total_institucion_canete, name='obtener_data_total_institucion_canete'),
    path('obtener_data_equipos_medicos_canete/', views.obtener_data_equipos_medicos_canete, name='obtener_data_equipos_medicos_canete'),
    path('obtener_data_equipos_industriales/', views.obtener_data_equipos_industriales, name='obtener_data_equipos_industriales'),
    path('obtener_data_vehiculos_canete/', views.obtener_data_vehiculos_canete, name='obtener_data_vehiculos_canete'),
    
    
    
    # Vistas Peticiones
    path('get_lebu_industrial/', views.get_lebu_industrial, name='get_lebu_industrial'),
    path('get_lebu_medico/', views.get_lebu_medico, name='get_lebu_medico'),
    path('get_lebu_vehiculos/', views.get_lebu_vehiculos, name='get_lebu_vehiculos'),
    
    # Vistas otras
    path('obtener_criticidad_medicos_lebu/', views.obtener_criticidad_medicos_lebu, name='obtener_criticidad_medicos_lebu'),
    
    
    # Vistas catastro
    path('añadir_catastro_industrial/', views.añadir_catastro_industrial, name='añadir_catastro_industrial'),
    path('anadir_catastro_vehiculos/', views.anadir_catastro_vehiculos, name='anadir_catastro_vehiculos'),
]

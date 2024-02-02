from django.urls import path
from . import views


urlpatterns = [
    # Eliminar catastros
    path('eliminar_catastro_arauco/', views.eliminar_catastro_arauco, name='eliminar_catastro_arauco'),
]
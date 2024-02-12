from django.urls import path
from . import views


urlpatterns = [
    # Eliminar catastros
    # path('eliminar_catastro_arauco/', views.eliminar_catastro_arauco, name='eliminar_catastro_arauco'),
    path('generar_pdf_catastro/', views.generar_pdf, name='generar_pdf_catastro'),
]
from django.shortcuts import render
from .models import Institucion
from django.contrib.auth.decorators import login_required


from django.conf import settings
from openpyxl import load_workbook



# Create your views here.

@login_required
def inicio_admin(request):
    instituciones = Institucion.objects.all()[:3]    

    return render(request, 'admin/inicio.html', {'instituciones': instituciones})

@login_required
def instituciones_admin(request):
    return render(request, 'admin/instituciones.html')







# Funciones utiles


    
    
    
    
    
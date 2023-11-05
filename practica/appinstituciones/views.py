from django.shortcuts import render
from .models import Institucion
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.core.paginator import Paginator

# from django.conf import settings

from appcatastro.models import CatastroEquipoIndustriales
from appcatastro.models import CatastroEquiposMedicos
from appcatastro.models import CatastroAmbulancias
from appautenticacion.models import CustomUser

# Create your views here.

@login_required
def inicio_admin(request):
    instituciones = Institucion.objects.all()[:1] 

    return render(request, 'admin/inicio.html', {'instituciones': instituciones})







@login_required
def lista_usuarios(request):
    # lista_usuarios = CustomUser.objects.filter(cargo='usuario').all()
    lista_usuarios = CustomUser.objects.all()
    
    paginator = Paginator(lista_usuarios, 20)
    page = request.GET.get('page')
    
    try:
        usuarios = paginator.page(page)
    except Exception:
        usuarios = paginator.page(1)
        
        
    return render(request, 'admin/usuarios.html', {'usuarios': usuarios})









@login_required
def instituciones_admin(request):
    return render(request, 'admin/instituciones.html')







# Funciones utiles
# graficos libreria: https://echarts.apache.org/examples/en/index.html#chart-type-bar
# Docs graficos: https://echarts.apache.org/en/option.html#grid.width

def obtener_grafico_institucion_lebu(request):
    estados_equipos_medicos = CatastroEquipoIndustriales.objects.values('estado')
    data_grafico = {
        'bueno': 0,
        'regular': 0,
        'malo': 0,
        'baja': 0
    }
    
    for e in estados_equipos_medicos: # Bueno - Regular - Malo - Baja
        if e['estado'] == 'BUENO':
            data_grafico['bueno'] += 1 
        elif e['estado'] == 'REGULAR':
            data_grafico['regular'] += 1
        elif e['estado'] == 'MALO':
            data_grafico['malo'] += 1
        elif e['estado'] == 'BAJA':
            data_grafico['baja'] += 1

    
    
    return JsonResponse(data_grafico)

def obtener_data_equipos_medicos_lebu(request):
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.values('estado')
    data = {
        'bueno': 0,
        'regular': 0,
        'malo': 0,
        'baja': 0
    }

    for e in data_estado_equipos_medicos:
        if e['estado'] == 'BUENO':
            data['bueno'] += 1 
        elif e['estado'] == 'REGULAR':
            data['regular'] += 1
        elif e['estado'] == 'MALO':
            data['malo'] += 1
        elif e['estado'] == 'BAJA':
            data['baja'] += 1

    return JsonResponse(data)


def obtener_data_ambulancias_lebu(requets):
    data_ambulancias = CatastroAmbulancias.objects.values('estado')
    data = {
        'bueno': 0,
        'regular': 0,
        'malo': 0,
        'baja': 0
    }

    for e in data_ambulancias:
        print(e)
        if e['estado'] == 'BUENO':
            data['bueno'] += 1 
        elif e['estado'] == 'REGULAR':
            data['regular'] += 1
        elif e['estado'] == 'MALO':
            data['malo'] += 1
        elif e['estado'] == 'BAJA':
            data['baja'] += 1

    return JsonResponse(data)


def obtener_data_total_lebu(request):
    data_ambulancias = CatastroAmbulancias.objects.values('estado')
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.values('estado')
    estados_equipos_medicos = CatastroEquipoIndustriales.objects.values('estado')

    data = {
        'bueno': 0,
        'regular': 0,
        'malo': 0,
        'baja': 0
    }
    
    for e in data_ambulancias:
        if e['estado'] == 'BUENO':
            data['bueno'] += 1 
        elif e['estado'] == 'REGULAR':
            data['regular'] += 1
        elif e['estado'] == 'MALO':
            data['malo'] += 1
        elif e['estado'] == 'BAJA':
            data['baja'] += 1
    
    for e in data_estado_equipos_medicos:
        if e['estado'] == 'BUENO':
            data['bueno'] += 1 
        elif e['estado'] == 'REGULAR':
            data['regular'] += 1
        elif e['estado'] == 'MALO':
            data['malo'] += 1
        elif e['estado'] == 'BAJA':
            data['baja'] += 1
            
    for e in estados_equipos_medicos: # Bueno - Regular - Malo - Baja
        if e['estado'] == 'BUENO':
            data['bueno'] += 1 
        elif e['estado'] == 'REGULAR':
            data['regular'] += 1
        elif e['estado'] == 'MALO':
            data['malo'] += 1
        elif e['estado'] == 'BAJA':
            data['baja'] += 1
            
    return JsonResponse(data)
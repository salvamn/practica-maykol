from django.shortcuts import render
from .models import Institucion
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect
# from django.conf import settings

from appcatastro.models import CatastroEquipoIndustriales
from appcatastro.models import CatastroEquiposMedicos
from appcatastro.models import CatastroAmbulancias
from appautenticacion.models import CustomUser
from appinstituciones.models import Institucion
from .models import Institucion

# Create your views here.

@login_required
def inicio_admin(request):
    instituciones = Institucion.objects.all()[:1] 

    return render(request, 'admin/inicio.html', {'instituciones': instituciones})







@login_required
def lista_usuarios(request):
    # lista_usuarios = CustomUser.objects.filter(cargo='usuario').all()
    lista_usuarios = CustomUser.objects.all()
    lista_instituciones = Institucion.objects.all()
    
    paginator = Paginator(lista_usuarios, 12)
    page = request.GET.get('page')
    
    try:
        usuarios = paginator.page(page)
    except Exception:
        usuarios = paginator.page(1)
        
        
    return render(request, 'admin/usuarios.html', {'usuarios': usuarios, 'instituciones': lista_instituciones})






















@login_required
def instituciones_admin(request, institucion, tipo_equipo=None):
    """Esta vista renderiza una institucion, esta institucion recibe dos argumentos: el nombre y tipo de equipo a mostrar
    
    - El primer argumento osea el nombre de la institucion es obligatorio
    - El segundo argumento es opcional
    
    
    """
    
    global data_tipo_equipo
    data_tipo_equipo = None
    
    if tipo_equipo is None and 'tipo_equipo' in request.GET:
        
        tipo_equipo = request.GET['tipo_equipo']
        
        if tipo_equipo == 'medico':
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
            
            data_tipo_equipo = data_grafico

    data_institucion = Institucion.objects.get(nombre=institucion)
    
    # lista_instituciones = Institucion.objects.all()
    select_tipo_equipo = ['medico', 'vehiculo', 'industrial']
    
    return render(request, 
                'admin/instituciones.html', {
                'institucion': data_institucion, 
                'tipo_equipo': select_tipo_equipo
                })
    
    
def get_lebu_industrial(request):
    datos = list(CatastroEquipoIndustriales.objects.values())
    return JsonResponse({'datos': datos})

def get_lebu_medico(request):
    datos = list(CatastroEquiposMedicos.objects.values())
    return JsonResponse({'datos': datos})

def get_lebu_vehiculos(request):
    datos = list(CatastroAmbulancias.objects.values())
    return JsonResponse({'datos': datos})























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


def obtener_criticidad_medicos_lebu(request):
    data_criticidad = CatastroEquiposMedicos.objects.values('criticidad') # CRITICO - RELEVANTE
    data = {
        'critico': 0,
        'relevante': 0
    }
    
    for crt in data_criticidad:
        if crt['criticidad'] == 'CRITICO':
            data['critico'] += 1
        elif crt['criticidad'] == 'RELEVANTE':
            data['relevante'] += 1
            
    return JsonResponse(data)
    
    
    



# Catastro


@login_required
def añadir_catastro_industrial(request):
    if request.method == 'POST':
        print(request.POST)
        print('Hola')
        servicio_clinico = request.POST.get('servicio-clinico', None)
        clase = request.POST.get('clase', None)
        sub_clase = request.POST.get('sub-clase', None)
        
        nombre_equipo = request.POST.get('nombre-equipo', None)
        marca = request.POST.get('marca', None)
        modelo = request.POST.get('modelo', None)
        
        serie = request.POST.get('serie', None)
        numero_inventario = request.POST.get('numero-inventario', None)
        propiedad = request.POST.get('propiedad', None)
        
        anio_adquisicion = request.POST.get('anio-adquisicion', None)
        vida_util = request.POST.get('vida-util', None)

        nuevo_equipo = CatastroEquipoIndustriales(
            servicio_clinico=servicio_clinico,
            recinto='',
            clase=clase,
            subclase=sub_clase,
            nombre_equipo=nombre_equipo,
            marca=marca,
            modelo=modelo,
            serie=serie,
            numero_inventario=numero_inventario,
            propio=propiedad,
            anio_adquisicion=anio_adquisicion,
            vida_util=vida_util
        )
        nuevo_equipo.save()
        messages.success(request, 'Equipo agregado con exito')
        return redirect('añadir_catastro_industrial')
        

        
    catastro_equipo_industrial = CatastroEquipoIndustriales.objects.values()
    return render(request, 'admin/añadir_catastro_industrial.html', {'equipos_industriales': catastro_equipo_industrial})


# def get_
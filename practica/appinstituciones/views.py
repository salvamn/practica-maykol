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
    # usuario_actual = request.user
    # lista_usuarios = CustomUser.objects.exclude(id=usuario_actual.id)
    lista_usuarios = CustomUser.objects.all()
    lista_instituciones = Institucion.objects.all()
    
    paginator = Paginator(lista_usuarios, 12)
    page = request.GET.get('page')
    
    try:
        usuarios = paginator.page(page)
    except Exception:
        usuarios = paginator.page(1)
        
        
    return render(request, 'admin/usuarios.html', {'usuarios': usuarios, 'instituciones': lista_instituciones})





















# Lebu id 1
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
            # estados_equipos_medicos = CatastroEquipoIndustriales.objects.values('estado')
            estados_equipos_medicos = CatastroEquipoIndustriales.objects.filter(id_institucion=1).values('estado')
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
                'admin/institucion_lebu.html', {
                'institucion': data_institucion, 
                'tipo_equipo': select_tipo_equipo
                })
def get_lebu_industrial(request):
    datos = list(CatastroEquipoIndustriales.objects.filter(id_institucion__isnull=True).values())
    return JsonResponse({'datos': datos})
def get_lebu_medico(request):
    datos = list(CatastroEquiposMedicos.objects.filter(id_institucion=1).values())
    return JsonResponse({'datos': datos})
def get_lebu_vehiculos(request):
    datos = list(CatastroAmbulancias.objects.filter(id_institucion=1).values())
    return JsonResponse({'datos': datos})

# Arauco id 2
@login_required
def institucion_arauco(request):
    return render(request, 'admin/instituciones/arauco.html')
def get_arauco_industrial(request):
    datos = list(CatastroEquipoIndustriales.objects.filter(id_institucion=2).values())
    return JsonResponse({'datos': datos})
def get_arauco_medico(request):
    datos = list(CatastroEquiposMedicos.objects.filter(id_institucion=2).values())
    return JsonResponse({'datos': datos})
def get_arauco_vehiculos(request):
    datos = list(CatastroAmbulancias.objects.filter(id_institucion=2).values())
    return JsonResponse({'datos': datos})

# Cañete id 4
@login_required
def institucion_canete(request):
    return render(request, 'admin/instituciones/canete.html')
def get_canete_industrial(request):
    datos = list(CatastroEquipoIndustriales.objects.filter(id_institucion=4).values())
    return JsonResponse({'datos': datos})
def get_canete_medico(request):
    datos = list(CatastroEquiposMedicos.objects.filter(id_institucion=4).values())
    return JsonResponse({'datos': datos})
def get_canete_vehiculos(request):
    datos = list(CatastroAmbulancias.objects.filter(id_institucion=4).values())
    return JsonResponse({'datos': datos})

# Curanilahue id 3
@login_required
def institucion_curanilahue(request):
    return render(request, 'admin/instituciones/curanilahue.html')
def get_curanilahue_industrial(request):
    datos = list(CatastroEquipoIndustriales.objects.filter(id_institucion=3).values())
    return JsonResponse({'datos': datos})
def get_curanilahue_medico(request):
    datos = list(CatastroEquiposMedicos.objects.filter(id_institucion=3).values())
    return JsonResponse({'datos': datos})
def get_curanilahue_vehiculos(request):
    datos = list(CatastroAmbulancias.objects.filter(id_institucion=3).values())
    return JsonResponse({'datos': datos})

# Contulmo id 5
@login_required
def institucion_contulmo(request):
    return render(request, 'admin/instituciones/contulmo.html')  
def get_contulmo_industrial(request):
    datos = list(CatastroEquipoIndustriales.objects.filter(id_institucion=5).values())
    return JsonResponse({'datos': datos})
def get_contulmo_medico(request):
    datos = list(CatastroEquiposMedicos.objects.filter(id_institucion=5).values())
    return JsonResponse({'datos': datos})
def get_contulmo_vehiculos(request):
    datos = list(CatastroAmbulancias.objects.filter(id_institucion=5).values())
    return JsonResponse({'datos': datos})    













# Funciones utiles
# graficos libreria: https://echarts.apache.org/examples/en/index.html#chart-type-bar
# Docs graficos: https://echarts.apache.org/en/option.html#grid.width

# Lebu
def obtener_grafico_institucion_lebu(request):
    # estados_equipos_medicos = CatastroEquipoIndustriales.objects.values('estado')
    estados_equipos_medicos = CatastroEquipoIndustriales.objects.filter(id_institucion__isnull=True).values('estado')
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
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.filter(id_institucion=1).values('estado')
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
    # data_ambulancias = CatastroAmbulancias.objects.values('estado')
    data_ambulancias = CatastroAmbulancias.objects.filter(id_institucion=1).values('estado')
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
    data_ambulancias = CatastroAmbulancias.objects.filter(id_institucion=1).values('estado')
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.filter(id_institucion=1).values('estado')
    estados_equipos_medicos = CatastroEquipoIndustriales.objects.filter(id_institucion__isnull=True).values('estado')

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
    
    
#  Arauco
def obtener_data_total_institucion_arauco(requets):
    data_ambulancias = CatastroAmbulancias.objects.filter(id_institucion=2).values('estado')
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.filter(id_institucion=2).values('estado')
    estados_equipos_medicos = CatastroEquipoIndustriales.objects.filter(id_institucion=2).values('estado')

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
def obtener_data_equipos_medicos_arauco(request):
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.filter(id_institucion=2).values('estado')
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
def obtener_data_equipos_industriales_arauco(request):
    estados_equipos_industriales = CatastroEquipoIndustriales.objects.filter(id_institucion=2).values('estado')
    data_grafico = {
        'bueno': 0,
        'regular': 0,
        'malo': 0,
        'baja': 0
    }
    
    for e in estados_equipos_industriales: # Bueno - Regular - Malo - Baja
        if e['estado'] == 'BUENO':
            data_grafico['bueno'] += 1 
        elif e['estado'] == 'REGULAR':
            data_grafico['regular'] += 1
        elif e['estado'] == 'MALO':
            data_grafico['malo'] += 1
        elif e['estado'] == 'BAJA':
            data_grafico['baja'] += 1

    return JsonResponse(data_grafico)
def obtener_data_vehiculos_arauco(request):
    data_ambulancias = CatastroAmbulancias.objects.filter(id_institucion=2).values('estado')
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


# Cañete
def obtener_data_total_institucion_canete(request):
    data_ambulancias = CatastroAmbulancias.objects.filter(id_institucion=4).values('estado')
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.filter(id_institucion=4).values('estado')
    estados_equipos_medicos = CatastroEquipoIndustriales.objects.filter(id_institucion=4).values('estado')

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
def obtener_data_equipos_medicos_canete(request):
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.filter(id_institucion=4).values('estado')
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
def obtener_data_equipos_industriales(request):
    estados_equipos_industriales = CatastroEquipoIndustriales.objects.filter(id_institucion=4).values('estado')
    data_grafico = {
        'bueno': 0,
        'regular': 0,
        'malo': 0,
        'baja': 0
    }
    
    for e in estados_equipos_industriales: # Bueno - Regular - Malo - Baja
        if e['estado'] == 'BUENO':
            data_grafico['bueno'] += 1 
        elif e['estado'] == 'REGULAR':
            data_grafico['regular'] += 1
        elif e['estado'] == 'MALO':
            data_grafico['malo'] += 1
        elif e['estado'] == 'BAJA':
            data_grafico['baja'] += 1

    return JsonResponse(data_grafico)
def obtener_data_vehiculos_canete(request):
    data_ambulancias = CatastroAmbulancias.objects.filter(id_institucion=4).values('estado')
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






# Usuarios
def obtener_usuario(request, usuario_id):
    usuario = CustomUser.objects.filter(id=usuario_id).values(
        'id',
        'first_name', 'last_name', 'username',
        'email', 'rut', 'cargo', 'institucion_id'   
    )
    usuario_serializado = {
        'id': usuario[0]['id'],
        'first_name': usuario[0]['first_name'],
        'last_name': usuario[0]['last_name'], 
        'username': usuario[0]['username'],
        'email': usuario[0]['email'], 
        'rut': usuario[0]['rut'], 
        'cargo': usuario[0]['cargo'], 
        'institucion_id': usuario[0]['institucion_id'] 
    }    
    return JsonResponse(usuario_serializado)

def eliminar_usuario(request, usuario_id):
    try:
        usuario_a_eliminar = CustomUser.objects.get(id=usuario_id)
        usuario_a_eliminar.delete()

        return JsonResponse({'data': 'usuario eliminado'})
    except CustomUser.DoesNotExist:
        return JsonResponse({'message': 'Usuario no encontrado'}, status=404)
    
    




# Catastro


@login_required
def añadir_catastro_industrial(request):
    if request.method == 'POST':
        # print(request.POST)
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
            clase=clase,
            subclase=sub_clase,
            nombre_equipo=nombre_equipo,
            marca=marca,
            modelo=modelo,
            serie=serie,
            numero_inventario=numero_inventario,
            propio=propiedad,
            anio_adquisicion=anio_adquisicion,
            vida_util=vida_util,
            
            # campos no utiles de momento
            vida_util_residual=0,
            recinto='',
            estado='',
            garantia='',
            anio_vencimiento_garantia=0,
            bajo_plan_mantenimiento=''
        )
        nuevo_equipo.save()
        messages.success(request, 'Equipo agregado con exito')
        return redirect('añadir_catastro_industrial')
        

        
    catastro_equipo_industrial = CatastroEquipoIndustriales.objects.values()
    return render(request, 'admin/añadir_catastro_industrial.html', {'equipos_industriales': catastro_equipo_industrial})


@login_required
def anadir_catastro_vehiculos(request):




    return render(request, 'admin/añadir_catastro_vehiculos.html')
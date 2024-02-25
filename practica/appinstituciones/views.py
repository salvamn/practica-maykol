from django.shortcuts import render
from .models import Institucion
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
# from django.conf import settings

from django.template.loader import get_template
from weasyprint import CSS
from weasyprint import HTML
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from django.conf import settings

from appcatastro.models import CatastroEquipoIndustriales
from appcatastro.models import CatastroEquiposMedicos
from appcatastro.models import CatastroAmbulancias
from appautenticacion.models import CustomUser
from appinstituciones.models import Institucion
from .models import Institucion
from .models import Convenios

import json
import os

# https://semantic-ui.com/collections/table.html

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

    paginator = Paginator(lista_usuarios, 8)
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
            estados_equipos_medicos = CatastroEquipoIndustriales.objects.filter(
                id_institucion=1).values('estado')
            data_grafico = {
                'bueno': 0,
                'regular': 0,
                'malo': 0,
                'baja': 0
            }

            for e in estados_equipos_medicos:  # Bueno - Regular - Malo - Baja
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
    datos = list(CatastroEquipoIndustriales.objects.filter(
        id_institucion=1).values())
    return JsonResponse({'datos': datos})


def get_lebu_medico(request):
    datos = list(CatastroEquiposMedicos.objects.filter(
        id_institucion=1).values())
    return JsonResponse({'datos': datos})


def get_lebu_vehiculos(request):
    datos = list(CatastroAmbulancias.objects.filter(id_institucion=1).values())
    return JsonResponse({'datos': datos})

# Arauco id 2


@login_required
def institucion_arauco(request):
    return render(request, 'admin/instituciones/arauco.html')


def get_arauco_industrial(request):
    datos = list(CatastroEquipoIndustriales.objects.filter(
        id_institucion=2).values())
    return JsonResponse({'datos': datos})


def get_arauco_medico(request):
    datos = list(CatastroEquiposMedicos.objects.filter(
        id_institucion=2).values())
    return JsonResponse({'datos': datos})


def get_arauco_vehiculos(request):
    datos = list(CatastroAmbulancias.objects.filter(id_institucion=2).values())
    return JsonResponse({'datos': datos})

# Cañete id 4


@login_required
def institucion_canete(request):
    return render(request, 'admin/instituciones/canete.html')


def get_canete_industrial(request):
    datos = list(CatastroEquipoIndustriales.objects.filter(
        id_institucion=4).values())
    return JsonResponse({'datos': datos})


def get_canete_medico(request):
    datos = list(CatastroEquiposMedicos.objects.filter(
        id_institucion=4).values())
    return JsonResponse({'datos': datos})


def get_canete_vehiculos(request):
    datos = list(CatastroAmbulancias.objects.filter(id_institucion=4).values())
    return JsonResponse({'datos': datos})

# Curanilahue id 3


@login_required
def institucion_curanilahue(request):
    return render(request, 'admin/instituciones/curanilahue.html')


def get_curanilahue_industrial(request):
    datos = list(CatastroEquipoIndustriales.objects.filter(
        id_institucion=3).values())
    return JsonResponse({'datos': datos})


def get_curanilahue_medico(request):
    datos = list(CatastroEquiposMedicos.objects.filter(
        id_institucion=3).values())
    return JsonResponse({'datos': datos})


def get_curanilahue_vehiculos(request):
    datos = list(CatastroAmbulancias.objects.filter(id_institucion=3).values())
    return JsonResponse({'datos': datos})

# Contulmo id 5


@login_required
def institucion_contulmo(request):
    return render(request, 'admin/instituciones/contulmo.html')


def get_contulmo_industrial(request):
    datos = list(CatastroEquipoIndustriales.objects.filter(
        id_institucion=5).values())
    return JsonResponse({'datos': datos})


def get_contulmo_medico(request):
    datos = list(CatastroEquiposMedicos.objects.filter(
        id_institucion=5).values())
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
    estados_equipos_medicos = CatastroEquipoIndustriales.objects.filter(
        id_institucion=1).values('estado')
    data_grafico = {
        'bueno': 0,
        'regular': 0,
        'malo': 0,
        'baja': 0
    }

    for e in estados_equipos_medicos:  # Bueno - Regular - Malo - Baja
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
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.filter(
        id_institucion=1).values('estado')
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
    data_ambulancias = CatastroAmbulancias.objects.filter(
        id_institucion=1).values('estado')
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
    data_ambulancias = CatastroAmbulancias.objects.filter(
        id_institucion=1).values('estado')
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.filter(
        id_institucion=1).values('estado')
    estados_equipos_medicos = CatastroEquipoIndustriales.objects.filter(
        id_institucion=1).values('estado')
    # estados_equipos_medicos = CatastroEquipoIndustriales.objects.filter(id_institucion=1).values('estado')

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

    for e in estados_equipos_medicos:  # Bueno - Regular - Malo - Baja
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
    data_criticidad = CatastroEquiposMedicos.objects.values(
        'criticidad')  # CRITICO - RELEVANTE
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
    data_ambulancias = CatastroAmbulancias.objects.filter(
        id_institucion=2).values('estado')
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.filter(
        id_institucion=2).values('estado')
    estados_equipos_medicos = CatastroEquipoIndustriales.objects.filter(
        id_institucion=2).values('estado')

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

    for e in estados_equipos_medicos:  # Bueno - Regular - Malo - Baja
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
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.filter(
        id_institucion=2).values('estado')
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
    estados_equipos_industriales = CatastroEquipoIndustriales.objects.filter(
        id_institucion=2).values('estado')
    data_grafico = {
        'bueno': 0,
        'regular': 0,
        'malo': 0,
        'baja': 0
    }

    for e in estados_equipos_industriales:  # Bueno - Regular - Malo - Baja
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
    data_ambulancias = CatastroAmbulancias.objects.filter(
        id_institucion=2).values('estado')
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
    data_ambulancias = CatastroAmbulancias.objects.filter(
        id_institucion=4).values('estado')
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.filter(
        id_institucion=4).values('estado')
    estados_equipos_medicos = CatastroEquipoIndustriales.objects.filter(
        id_institucion=4).values('estado')

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

    for e in estados_equipos_medicos:  # Bueno - Regular - Malo - Baja
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
    data_estado_equipos_medicos = CatastroEquiposMedicos.objects.filter(
        id_institucion=4).values('estado')
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
    estados_equipos_industriales = CatastroEquipoIndustriales.objects.filter(
        id_institucion=4).values('estado')
    data_grafico = {
        'bueno': 0,
        'regular': 0,
        'malo': 0,
        'baja': 0
    }

    for e in estados_equipos_industriales:  # Bueno - Regular - Malo - Baja
        if e['estado'] == 'BUENO':
            data_grafico['bueno'] += 1
        elif e['estado'] == 'REGULAR':
            data_grafico['regular'] += 1
        elif e['estado'] == 'MALO':
            data_grafico['malo'] += 1
        elif e['estado'] == 'BAJA':
            data_grafico['baja'] += 1

    return JsonResponse(dict(data_grafico))


def obtener_data_vehiculos_canete(request):
    data_ambulancias = CatastroAmbulancias.objects.filter(
        id_institucion=4).values('estado')
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

# Get data catastro ganeral


def obtener_data_catastro_vehiculos_general(request):
    data = CatastroAmbulancias.objects.values()
    return JsonResponse(list(data), safe=False)


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


def editar_usuario(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('id-usuario')
        usuario = CustomUser.objects.get(id=id_usuario)

        nuevo_nombre = request.POST.get('nuevo-nombre', None)
        nuevo_apellido = request.POST.get('nuevo-apellido', None)
        nuevo_nombre_usuario = request.POST.get('nuevo-nombre-usuario', None)
        nuevo_correo = request.POST.get('nuevo-correo', None)
        nuevo_rut = request.POST.get('nuevo-rut', None)
        nueva_institucion = request.POST.get('institucion', None)
        nuevo_cargo = request.POST.get('cargo', None)

        # DONE Verficiar que el rut ingresado no exista y no sea de otro usuario.
        if nuevo_rut != usuario.rut:
            if CustomUser.objects.filter(rut=nuevo_rut).exists():
                messages.error(
                    request, 'El rut ya existe y pertenece a otro usuario.')
                return redirect('lista_usuarios')
        else:
            messages.error(
                request, 'El rut escrito es el mismo del usuario actual.')
            return redirect('lista_usuarios')

        # TODO Verificar que el correo electronico no exista o no corresponda a otro usuario

        if nuevo_nombre is not None and nuevo_nombre != '':
            usuario.first_name = nuevo_nombre
        if nuevo_apellido is not None and nuevo_apellido != '':
            usuario.last_name = nuevo_apellido
        if nuevo_nombre_usuario is not None and nuevo_nombre_usuario != '':
            usuario.username = nuevo_nombre_usuario
        if nuevo_correo is not None and nuevo_correo != '':
            usuario.email = nuevo_correo
        if nuevo_rut is not None and nuevo_rut != '':
            usuario.rut = nuevo_rut
        if nueva_institucion is not None and nueva_institucion != '':
            usuario.institucion_id = nueva_institucion
        if nuevo_cargo is not None and nuevo_cargo != '':
            usuario.cargo = nuevo_cargo

        usuario.save()
        messages.success(request, 'Usuario editado con exito.')
        return redirect('lista_usuarios')


# Catastro


@login_required
def anadir_catastro_industrial(request):
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

        institucion = request.POST.get('institucion', None)

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
            id_institucion=int(institucion),

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
    if request.method == 'POST':
        carroceria = request.POST.get('carroceria', None)
        clase = request.POST.get('clase', None)
        samu = request.POST.get('samu', None)
        funcion = request.POST.get('funcion', None)
        marca = request.POST.get('marca', None)
        modelo = request.POST.get('modelo', None)
        kilometraje = request.POST.get('kilometraje', None)
        criticidad = request.POST.get('criticidad', None)
        propiedad = request.POST.get('propiedad', None)
        patente = request.POST.get('patente', None)
        numero_motor = request.POST.get('numero-motor', None)
        id_institucion = request.POST.get('institucion', None)
        estado = request.POST.get('estado', None)

        print(request.POST)

        nuevo_vehiculo = CatastroAmbulancias(
            carroceria=carroceria,
            clase=clase,
            samu=samu,
            funcion=funcion,
            marca=marca,
            modelo=modelo,
            kilometraje=kilometraje,
            criticidad=criticidad,
            propietario=propiedad,
            patente=patente,
            numero_motor=numero_motor,
            estado=estado,
            id_institucion=id_institucion,

            # Datos no importantes de momento
            ubicacion='',
            sub_ubicacion='',
            anio=2023,
            vida_util=0,
            vencimiento_garantia='',
            plan_mantencion=0,
            tipo_equipo='',
            id_convenio=0,
            eliminado=0,
            garantia=0
        )
        nuevo_vehiculo.save()
        messages.success(request, 'Vehiculo agregado con exito')
        return redirect('anadir_catastro_vehiculos')

    catastro_equipo_vehiculos = CatastroAmbulancias.objects.values()
    return render(request, 'admin/añadir_catastro_vehiculos.html', {'data': catastro_equipo_vehiculos})


@login_required
def anadir_catastro_medicos(request):

    catastro_equipo_medico = CatastroEquiposMedicos.objects.values()
    return render(request, 'admin/añadir_catastro_medicos.html', {'data': catastro_equipo_medico})


# Convenios
@login_required
def convenios(request):
    if request.method == 'POST':
        servicio_salud = request.POST.get('servicio-salud', None)
        nombre_convenio = request.POST.get('nombre-convenio', None)
        fecha_resolucion = request.POST.get('fecha-resolucion', None)
        monto_anual = request.POST.get('monto-anual', None)
        subsignacion_sigfe = request.POST.get('subsignacion-sigfe', None)
        establecimiento = request.POST.get('establecimiento', None)
        fecha_expiracion = request.POST.get('fecha-expiracion', None)
        orden_compra = request.POST.get('orden-compra', None)
        tipo = request.POST.get('tipo', None)
        institucion_id = request.POST.get('institucion', None)

        nuevo_convenio = Convenios(
            servicio_salud=servicio_salud,
            nombre_convenio=nombre_convenio,
            fecha_resolucion=fecha_resolucion,
            fecha_expiracion=fecha_expiracion,
            monto_anual=monto_anual,
            subsignacion_sigfe=subsignacion_sigfe,
            establecimiento=establecimiento,
            orden_compra=orden_compra,
            id_institucion=institucion_id,
            tipo=tipo
        )
        nuevo_convenio.save()
        messages.success(request, 'Convenio agregado con exito.')
        return redirect('convenios')

    lista_intituciones = Institucion.objects.all()
    return render(request, 'admin/convenios.html', {'instituciones': lista_intituciones})


def obtener_convenios_general(request):
    convenios = Convenios.objects.all().order_by('-servicio_salud')
    convenios_serializados = serialize('json', convenios)

    return JsonResponse({'data': convenios_serializados}, safe=False)


@csrf_exempt
def eliminar_convenio(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        convenio_eliminar = Convenios.objects.filter(id=data['id'])

        if convenio_eliminar.exists():
            convenio_eliminar.delete()

            # TODO: retornar mensaje

            return JsonResponse({'mensaje': 'ok'})
    else:
        return JsonResponse({'mensaje': 'error'})


@csrf_exempt
def editar_convenio(request):
    if request.method == 'POST':
        # data = json.loads(request.body)
        id = request.POST.get('id', '')

        convenio_editar = Convenios.objects.filter(id=id)

        if convenio_editar.exists():
            # Los nombres deben ser identicos a los nombres de cada columna de la tabla Convenios de la base de datos
            datos_a_modificar = {
                'servicio_salud': request.POST.get('servicio_salud', ''),
                'nombre_convenio': request.POST.get('nombre_convenio', ''),
                'fecha_resolucion': request.POST.get('fecha_resolucion', ''),
                'fecha_experiracion': request.POST.get('fecha_experiracion', ''),
                'monto_anual': request.POST.get('monto_anual', ''),
                'subsignacion_sigfe': request.POST.get('subsignacion_sigfe', ''),
                'establecimiento': request.POST.get('establecimiento', ''),
                'orden_compra': request.POST.get('orden_compra', ''),
                'id_institucion': request.POST.get('id_institucion', ''),
                'tipo': request.POST.get('tipo', ''),
            }

            datos_a_modificar = {
                campo: valor for campo, valor in datos_a_modificar.items() if valor is not ''}
            convenio = Convenios.objects.get(id=id)

            for campo, valor in datos_a_modificar.items():
                setattr(convenio, campo, valor)

            convenio.save()

            messages.success(request, 'Equipo modificado')
            return redirect('convenios')


@login_required
@csrf_exempt
def generar_pdf_convenio(request):
    convenio = None
    data = json.loads(request.body)
    id = data['id']

    convenio = Convenios.objects.filter(id=id)
    if convenio.exists():
        convenio = Convenios.objects.get(id=id)
        contexto = {
            'convenio': convenio
        }

        template = get_template('admin/pdf/pdf_convenio.html')
        html = template.render(contexto)
        response = HttpResponse(content_type='application/pdf')
        filename = f'pdfconvenio-{data["id"]}'
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        css_url = os.path.join(
            settings.BASE_DIR, 'appinstituciones\static\css\pdf_css\pdf_catastro.css')

        html = HTML(string=html)
        result = html.write_pdf(encoding='utf-8', stylesheets=[CSS(css_url)])
        response.write(result)

        return response


# Busquedas de data de instituciones
@csrf_exempt
def busqueda_equipos_medicos(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        # desenpaquetar la data
        id_institucion = data['id_institucion']
        tipo_equipo = data['tipo_equipo']
        numero_inventario_busqueda = data['numero_inventario_busqueda']

        try:
            resultado = CatastroEquiposMedicos.objects.filter(
                id_institucion=id_institucion, tipo_equipo=tipo_equipo, numero_inventario=numero_inventario_busqueda)
            return JsonResponse({'data': list(resultado.values())})
        except Exception as e:
            print(e)


@csrf_exempt
def busqueda_equipos_industriales(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        # desenpaquetar la data
        id_institucion = data['id_institucion']
        tipo_equipo = data['tipo_equipo']
        numero_inventario_busqueda = data['numero_inventario_busqueda']

        try:
            resultado = CatastroEquipoIndustriales.objects.filter(
                id_institucion=id_institucion, tipo_equipo=tipo_equipo, numero_inventario=numero_inventario_busqueda)
            return JsonResponse({'data': list(resultado.values())})
        except Exception as e:
            print(e)


@csrf_exempt
def busqueda_vehiculos(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)

        # desenpaquetar la data
        id_institucion = data['id_institucion']
        tipo_equipo = data['tipo_equipo']
        patente = data['numero_inventario_busqueda']

        try:
            resultado = CatastroAmbulancias.objects.filter(
                id_institucion=id_institucion, tipo_equipo=tipo_equipo, patente=patente)
            print(resultado)
            return JsonResponse({'data': list(resultado.values())})
        except Exception as e:
            print(e)


# Crud Eliminar Catastros
@csrf_exempt
def eliminar_catastro(request):
    if request.method == 'POST':
        # Convertimos la data recibida a un json que es equivalente a un diccionario de python
        data = json.loads(request.body.decode('utf-8'))

        # desnpaquetamos la data
        id = data['id']
        id_institucion = data['idInstitucion']
        tipo_equipo = data['tipoEquipo']

        # verificamos el tipo de equipo
        if tipo_equipo == 'medico':
            # buscamos en la db el equipo a eliminar
            equipo = CatastroEquiposMedicos.objects.filter(
                id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)

            # si el equipo existe lo eliminamos
            if equipo.exists():
                equipo.delete()
                return JsonResponse({'mensaje': f'Equipo con id: {id} eliminado con exito.', 'categoria': 'success'})

        # repetimos para los otros tipos de equipos.
        elif tipo_equipo == 'industrial':
            equipo = CatastroEquipoIndustriales.objects.filter(
                id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)

            if equipo.exists():
                equipo.delete()
                return JsonResponse({'mensaje': f'Equipo con: {id} eliminado con exito.', 'categoria': 'success'})

        elif tipo_equipo == 'vehiculo':
            equipo = CatastroAmbulancias.objects.filter(
                id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)

            if equipo.exists():
                equipo.delete()
                return JsonResponse({'mensaje': f'Equipo con: {id} eliminado con exito.', 'categoria': 'success'})


# Crud editar catastro
@csrf_exempt
def obtener_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        id = data['id']
        id_institucion = data['idInstitucion']
        tipo_equipo = data['tipoEquipo']

        if tipo_equipo == 'medico':
            # equipo = CatastroEquiposMedicos.objects.filter(id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)
            equipo = CatastroEquiposMedicos.objects.get(
                id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)

            # if equipo.exists():
            equipo_encontrado = {
                'id': equipo.id,
                'clase': equipo.clase,
                'nombre': equipo.nombre,
                'marca': equipo.marca,
                'modelo': equipo.modelo,
                'serie': equipo.serie,
                'anio': equipo.anio,
                'vida_util': equipo.vida_util,
                'estado': equipo.estado,
                'criticidad': equipo.criticidad,
                'garantia': equipo.garantia,
                'vencimiento_garantia': equipo.vencimiento_garantia,
                'plan_mantencion': equipo.plan_mantencion,
                'tipo_equipo': equipo.tipo_equipo,
                'id_convenio': equipo.id_convenio,
                'id_institucion': equipo.id_institucion,
                'eliminado': equipo.eliminado,
                'anio_ingreso': equipo.anio_ingreso,
                'costo_anual': equipo.costo_anual,
                'nombre_proveedor': equipo.nombre_proveedor,
                'numero_inventario': equipo.numero_inventario,
                'recinto': equipo.recinto,
                'servicio_clinico': equipo.servicio_clinico,
                'subclase': equipo.subclase,
                'tipo_mantenimiento': equipo.tipo_mantenimiento,
                'vida_util_residual': equipo.vida_util_residual
            }

            return JsonResponse({'resultado': equipo_encontrado})

        elif tipo_equipo == 'industrial':
            equipo = CatastroEquipoIndustriales.objects.get(
                id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)

            equipo_encontrado = {
                'id': equipo.id,
                'clase': equipo.clase,
                'subclase': equipo.subclase,
                'marca': equipo.marca,
                'modelo': equipo.modelo,
                'serie': equipo.serie,
                'numero_inventario': equipo.numero_inventario,
                'vida_util': equipo.vida_util,
                'vida_util_residual': equipo.vida_util_residual,
                'estado': equipo.estado,
                'garantia': equipo.garantia,
                'id_institucion': equipo.id_institucion,
                'anio': equipo.anio,
                'anio_ingreso_plan_mantenimiento': equipo.anio_ingreso_plan_mantenimiento,
                'costo_anual_mantenimiento': equipo.costo_anual_mantenimiento,
                'criticidad': equipo.criticidad,
                'eliminado': equipo.eliminado,
                'id_convenio_mantenimiento': equipo.id_convenio_mantenimiento,
                'nombre': equipo.nombre,
                'nombre_proveedor': equipo.nombre_proveedor,
                'nombre_recinto': equipo.nombre_recinto,
                'plan_mantencion': equipo.plan_mantencion,
                'tipo_equipo': equipo.tipo_equipo,
                'tipo_mantenimiento': equipo.tipo_mantenimiento,
                'ubicacion': equipo.ubicacion,
                'vencimiento_garantia': equipo.vencimiento_garantia,
            }

            return JsonResponse({'resultado': equipo_encontrado})

        elif tipo_equipo == 'vehiculo':
            equipo = CatastroAmbulancias.objects.get(
                id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)

            equipo_encontrado = {
                'id': equipo.id,
                'samu': equipo.samu,
                'funcion': equipo.funcion,
                'marca': equipo.marca,
                'modelo': equipo.modelo,
                'patente': equipo.patente,
                'numero_motor': equipo.numero_motor,
                'kilometraje': equipo.kilometraje,
                'estado': equipo.estado,
                'anio': equipo.anio,
                'vida_util': equipo.vida_util,
                'criticidad': equipo.criticidad,
                'garantia': equipo.garantia,
                'vencimiento_garantia': equipo.vencimiento_garantia,
                'plan_mantencion': equipo.plan_mantencion,
                'tipo_equipo': equipo.tipo_equipo,
                'id_institucion': equipo.id_institucion,
                'eliminado': equipo.eliminado,
                'anio_ingreso_plan_mantenimiento': equipo.anio_ingreso_plan_mantenimiento,
                'clase_ambulancia': equipo.clase_ambulancia,
                'costo_anual_mantenimiento': equipo.costo_anual_mantenimiento,
                'establecimiento': equipo.establecimiento,
                'estado_situacion': equipo.estado_situacion,
                'id_convenio_mantenimiento': equipo.id_convenio_mantenimiento,
                'nombre_proveedor': equipo.nombre_proveedor,
                'region': equipo.region,
                'tipo_ambulancia': equipo.tipo_ambulancia,
                'tipo_carroceria': equipo.tipo_carroceria,
                'tipo_mantenimiento': equipo.tipo_mantenimiento,
                'vida_util_residual': equipo.vida_util_residual,
            }

            return JsonResponse({'resultado': equipo_encontrado})


@csrf_exempt
def editar_equipo(request):
    if request.method == 'POST':
        print(request.POST)
        # Obtenemos datos escenciales para saber el tipo de equipo que editaremos
        tipo_equipo = request.POST.get('hidden-tipo-equipo', None)
        id_equipo = request.POST.get('hidden-id-equipo', None)

        # verificamos el tipo de equipo
        if tipo_equipo == 'medico':
            # obtenemos el equipo
            equipo = CatastroEquiposMedicos.objects.filter(id=id_equipo)

            # verificamos si el equipo existe
            if equipo.exists():
                # obtenemos toda la data de la peticion y la guardamos en un diccionario

                datos_a_modificar = {
                    'clase': request.POST.get('clase', ''),
                    'nombre': request.POST.get('nombre', ''),
                    'marca': request.POST.get('marca', ''),
                    'modelo': request.POST.get('modelo', ''),
                    'serie': request.POST.get('serie', ''),
                    'anio': request.POST.get('anio', ''),
                    'vida_util': request.POST.get('vida-util', ''),
                    'estado': request.POST.get('estado', ''),
                    'criticidad': request.POST.get('criticidad', ''),
                    'garantia': request.POST.get('garantia', ''),
                    'vencimiento_garantia': request.POST.get('vencimiento-garantia', ''),
                    'plan_mantencion': request.POST.get('plan-mantencion', ''),
                    'tipo_equipo': request.POST.get('tipo-equipo', ''),
                    'id_convenio': request.POST.get('id-convenio', ''),
                    'id_institucion': request.POST.get('id-institucion', ''),
                    'eliminado': request.POST.get('eliminado', ''),
                    'anio_ingreso': request.POST.get('anio-ingreso', ''),
                    'costo_anual': request.POST.get('costo-anual', ''),
                    'nombre_proveedor': request.POST.get('nombre-proveedor', ''),
                    'numero_inventario': request.POST.get('numero-inventario', ''),
                    'recinto': request.POST.get('recinto', ''),
                    'servicio_clinico': request.POST.get('servicio-clinico', ''),
                    'sub_clase': request.POST.get('sub-clase', ''),
                    'tipo_mantenimiento': request.POST.get('tipo-mantenimiento', ''),
                    'vida_util_residual': request.POST.get('vida-util-residual', ''),
                }

                #
                datos_a_modificar = {
                    campo: valor for campo, valor in datos_a_modificar.items() if valor is not ''}

                # obtenemos el equipo a editar
                equipo = CatastroEquiposMedicos.objects.get(id=id_equipo)

                # modificamos los campos mediante un for
                for campo, valor in datos_a_modificar.items():
                    setattr(equipo, campo, valor)

                # guardamos los datos modificados
                equipo.save()
                messages.success(request, 'Equipo modificado')

        elif tipo_equipo == 'industrial':
            equipo = CatastroEquipoIndustriales.objects.filter(id=id_equipo)

            if equipo.exists():

                datos_a_modificar = {
                    'clase': request.POST.get('clase', ''),
                    'subclase': request.POST.get('sub-clase', ''),
                    'marca': request.POST.get('marca', ''),
                    'modelo': request.POST.get('modelo', ''),
                    'serie': request.POST.get('serie', ''),
                    'numero_inventario': request.POST.get('numero-inventario', ''),
                    'vida_util': request.POST.get('vida-util', ''),
                    'vida_util_residual': request.POST.get('vida-util-residual', ''),
                    'estado': request.POST.get('estado', ''),
                    'garantia': request.POST.get('garantia', ''),
                    'id_institucion': request.POST.get('id-institucion', ''),
                    'anio': request.POST.get('anio', ''),
                    'anio_ingreso_plan_mantenimiento': request.POST.get('anio-ingreso', ''),
                    'costo_anual_mantenimiento': request.POST.get('costo-anual', ''),
                    'criticidad': request.POST.get('criticidad', ''),
                    'eliminado': request.POST.get('eliminado', ''),
                    'id_convenio_mantenimiento': request.POST.get('id-convenio', ''),
                    'nombre': request.POST.get('nombre', ''),
                    'nombre_proveedor': request.POST.get('nombre-proveedor', ''),
                    'nombre_recinto': request.POST.get('recinto', ''),
                    'plan_mantencion': request.POST.get('plan-mantencion', ''),
                    'tipo_equipo': request.POST.get('tipo-equipo', ''),
                    'tipo_mantenimiento': request.POST.get('tipo-mantenimiento', ''),
                    'ubicacion': request.POST.get('servicio-clinico', ''),
                    'vencimiento_garantia': request.POST.get('vencimiento-garantia', ''),
                }

                datos_a_modificar = {
                    campo: valor for campo, valor in datos_a_modificar.items() if valor is not ''}
                equipo = CatastroEquipoIndustriales.objects.get(id=id_equipo)

                for campo, valor in datos_a_modificar.items():
                    setattr(equipo, campo, valor)

                equipo.save()
                messages.success(request, 'Equipo modificado')

        elif tipo_equipo == 'vehiculo':
            equipo = CatastroAmbulancias.objects.filter(id=id_equipo)
            print(f'tipo de equipo: {tipo_equipo}')
            print(f'id: {id_equipo}')
            if equipo.exists():
                datos_a_modificar = {
                    'samu': request.POST.get('samu', ''),
                    'funcion': request.POST.get('funcion', ''),
                    'marca': request.POST.get('marca', ''),
                    'modelo': request.POST.get('modelo', ''),
                    'patente': request.POST.get('patente', ''),
                    'numero_motor': request.POST.get('numero-motor', ''),
                    'kilometraje': request.POST.get('kilometraje', ''),
                    'estado': request.POST.get('estado', ''),
                    'anio': request.POST.get('anio', ''),
                    'vida_util': request.POST.get('vida-util', ''),
                    'criticidad': request.POST.get('criticidad', ''),
                    'garantia': request.POST.get('garantia', ''),
                    'vencimiento_garantia': request.POST.get('vencimiento-garantia', ''),
                    'plan_mantencion': request.POST.get('plan-mantencion', ''),
                    'tipo_equipo': request.POST.get('tipo_equipo', ''),
                    'id_institucion': request.POST.get('id-institucion', ''),
                    'eliminado': request.POST.get('eliminado', ''),
                    'anio_ingreso_plan_mantenimiento': request.POST.get('anio-ingreso-plan-mantenimiento', ''),
                    'clase_ambulancia': request.POST.get('clase-ambulancia', ''),
                    'costo_anual_mantenimiento': request.POST.get('costo-anual-mantenimiento', ''),
                    'establecimiento': request.POST.get('establecimiento', ''),
                    'estado_situacion': request.POST.get('estado-situacion', ''),
                    'id_convenio_mantenimiento': request.POST.get('id-convenio-mantenimiento', ''),
                    'nombre_proveedor': request.POST.get('nombre-proveedor', ''),
                    'region': request.POST.get('region', ''),
                    'tipo_ambulancia': request.POST.get('tipo-ambulancia', ''),
                    'tipo_carroceria': request.POST.get('tipo-carroceria', ''),
                    'tipo_mantenimiento': request.POST.get('tipo-mantenimiento', ''),
                    'vida_util_residual': request.POST.get('vida-util-residual', ''),
                }

                datos_a_modificar = {
                    campo: valor for campo, valor in datos_a_modificar.items() if valor is not ''}
                equipo = CatastroAmbulancias.objects.get(id=id_equipo)

                for campo, valor in datos_a_modificar.items():
                    setattr(equipo, campo, valor)

                equipo.save()
                messages.success(request, 'Equipo modificado')

    url = reverse('instituciones_admin', args=['Lebu', 'medico'])
    return redirect(url)

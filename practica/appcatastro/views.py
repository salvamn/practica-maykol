from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings

from models import CatastroEquipoIndustriales
from models import CatastroEquiposMedicos
from models import CatastroAmbulancias
from appautenticacion.models import CustomUser

import json


# Crud Eliminar Catastros
@csrf_exempt
def eliminar_catastro_arauco(request):
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
            equipo = CatastroEquiposMedicos.objects.filter(id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)
            
            # si el equipo existe lo eliminamos
            if equipo.exists():
                equipo.delete()
                return JsonResponse({'mensaje': f'Equipo con id: {id} eliminado con exito.', 'categoria': 'success'})
            
        # repetimos para los otros tipos de equipos.
        elif tipo_equipo == 'industrial':
            equipo = CatastroEquipoIndustriales.objects.filter(id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)
            
            if equipo.exists():
                equipo.delete()
                return JsonResponse({'mensaje': f'Equipo con: {id} eliminado con exito.', 'categoria': 'success'})
        
        elif tipo_equipo == 'vehiculo':
            equipo = CatastroAmbulancias.objects.filter(id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)
            
            if equipo.exists():
                equipo.delete()
                return JsonResponse({'mensaje': f'Equipo con: {id} eliminado con exito.', 'categoria': 'success'})  
        
        
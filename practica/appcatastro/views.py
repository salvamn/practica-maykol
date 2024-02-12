from weasyprint import CSS
from weasyprint import HTML
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from django.http import FileResponse
from django.template.loader import get_template


# from models import CatastroEquipoIndustriales
from .models import CatastroEquiposMedicos
# from models import CatastroAmbulancias
# from appautenticacion.models import CustomUser

import json
import os

# os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
# https://stackoverflow.com/questions/63449770/oserror-cannot-load-library-gobject-2-0-error-0x7e
GTK_FOLDER = r'C:\Program Files\GTK3-Runtime Win64\bin'
os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')


# HTML('https://weasyprint.org/').write_pdf('weasyprint-website.pdf')
# # Crud Eliminar Catastros
# @csrf_exempt
# def eliminar_catastro_arauco(request):
#     if request.method == 'POST':
#         # Convertimos la data recibida a un json que es equivalente a un diccionario de python
#         data = json.loads(request.body.decode('utf-8'))

#         # desnpaquetamos la data
#         id = data['id']
#         id_institucion = data['idInstitucion']
#         tipo_equipo = data['tipoEquipo']

#         # verificamos el tipo de equipo
#         if tipo_equipo == 'medico':
#             # buscamos en la db el equipo a eliminar
#             equipo = CatastroEquiposMedicos.objects.filter(id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)

#             # si el equipo existe lo eliminamos
#             if equipo.exists():
#                 equipo.delete()
#                 return JsonResponse({'mensaje': f'Equipo con id: {id} eliminado con exito.', 'categoria': 'success'})

#         # repetimos para los otros tipos de equipos.
#         elif tipo_equipo == 'industrial':
#             equipo = CatastroEquipoIndustriales.objects.filter(id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)

#             if equipo.exists():
#                 equipo.delete()
#                 return JsonResponse({'mensaje': f'Equipo con: {id} eliminado con exito.', 'categoria': 'success'})

#         elif tipo_equipo == 'vehiculo':
#             equipo = CatastroAmbulancias.objects.filter(id=id, id_institucion=id_institucion, tipo_equipo=tipo_equipo)

#             if equipo.exists():
#                 equipo.delete()
#                 return JsonResponse({'mensaje': f'Equipo con: {id} eliminado con exito.', 'categoria': 'success'})


@csrf_exempt
@login_required
def generar_pdf(request):
    # https://youtu.be/11poEbQAqpU
    if request.method == 'POST':
        catastro = None
        data = json.loads(request.body)
        print(data)

        if data['tipoEquipo'] == 'medico':
            equipo = CatastroEquiposMedicos.objects.get(
                id=data['id'], tipo_equipo=data['tipoEquipo'])
            print(equipo)
            catastro = {
                'catastro': equipo
            }
            
        

        template = get_template('admin/pdf/pdf_catastro.html')
        html = template.render(catastro)
        response = HttpResponse(content_type='application/pdf')
        filename = f'pdfcatastro-{data["tipoEquipo"]}-{data["id"]}'
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        css_url = os.path.join(
            settings.BASE_DIR, 'appinstituciones\static\css\pdf_css\pdf_catastro.css')
        # print(settings.BASE_DIR)
        print(css_url)

        html = HTML(string=html)
        result = html.write_pdf(encoding='utf-8', stylesheets=[CSS(css_url)])
        # result = html.write_pdf(encoding='utf-8')
        response.write(result)

        return response

        # return render(request, 'admin/pdf/pdf_catastro.html')
    else:
        # Maneja el caso en que el método de la solicitud no sea POST
        # Puedes devolver un HttpResponseBadRequest u otra respuesta adecuada
        return HttpResponseBadRequest()

    # template = get_template('admin/pdf/pdf_catastro.html')
    # html = template.render()
    # response = HttpResponse(content_type='application/pdf')
    # filename = f'pdfcatastro.pdf'
    # response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # css_url = os.path.join(
    #     settings.BASE_DIR, 'appinstituciones\static\css\pdf_css\pdf_catastro.css')
    # # print(settings.BASE_DIR)
    # print(css_url)

    # html = HTML(string=html).write_pdf(
    #     encoding='utf-8', stylesheets=[CSS(css_url)])
    # response.write(html)

    # return response

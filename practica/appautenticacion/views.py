from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template.loader import get_template
from django.conf import settings
from django.urls import reverse


from .models import CustomUser
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from itertools import cycle
import sys
# Create your views here.

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('inicio_admin')
    
    if request.method == 'POST':
        rut = request.POST['rut']
        password = request.POST['password']
        user = authenticate(request, rut=rut, password=password)
        
        if user is not None:
            login(request, user)
            
            if request.user.cargo == 'administrador':
                return redirect('inicio_admin')
            elif request.user.cargo == 'usuario':
                pass
            
        else:
            messages.error(request, 'el rut o contraseña son incorrectos')
            return redirect('iniciar_sesion')

    
    return render(request, 'iniciar_sesion.html')


def cerrar_sesion(request):
    if request.user != None:
        logout(request)
        return redirect('/')


def crear_usuario(request):
    # Generador de rut: https://jqueryrut.sourceforge.net/generador-de-ruts-chilenos-validos.html
    if request.method == 'POST':
        print(request.POST)
        nombre_usuario = request.POST['nombre-usuario']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        rut = request.POST['rut']
        correo = request.POST['correo']
        contrasenia = request.POST['contrasenia']
        cargo = request.POST['cargo']
        institucion_id = request.POST['institucion']
        
        personas_con_rut = CustomUser.objects.filter(rut=rut)
        
         # Verificar si ya existe un usuario con el mismo nombre de usuario
        if CustomUser.objects.filter(username=nombre_usuario).exists():
            messages.error(request, 'El nombre de usuario ya existe')
            return redirect('lista_usuarios')

        if personas_con_rut.exists():
            messages.error(request, 'El rut ya existe en nuestra base de datos')
            return redirect('lista_usuarios')
        
        validar_rut = verificar_rut(rut)
        if validar_rut == False:
            messages.error(request, 'El rut ingresado es invalido.')
            return redirect('lista_usuarios')
        

        
        try:
            usuario = CustomUser.objects.create(
            username=nombre_usuario,
            first_name=nombre,
            last_name=apellido,
            rut=rut,
            email=correo,
            cargo=cargo,
            password=contrasenia,
            institucion_id=institucion_id
            )
            usuario.set_password(contrasenia)
            usuario.save()
        except Exception as e:
            print(e)
        
        
        
        
        messages.success(request, 'Usuario creado con exito.')
        return redirect('lista_usuarios')
    
    
    
def verificar_rut(rut):
    #https://www.lawebdelprogramador.com/codigo/Python/3532-Valida-Rut-Chile.html
	rut = rut.upper();
	rut = rut.replace("-","")
	rut = rut.replace(".","")
	aux = rut[:-1]
	dv = rut[-1:]
 
	revertido = map(int, reversed(str(aux)))
	factors = cycle(range(2,8))
	s = sum(d * f for d, f in zip(revertido,factors))
	res = (-s)%11
 
	if str(res) == dv:
		return True
	elif dv=="K" and res==10:
		return True
	else:
		return False






# Vistas para recuperar la contraseña
def enviar_correo(rut):
    # Obtenemos el usario por su rut
    # https://youtu.be/WDxHPd1aIVE problemas con correo
    # usuario_actual = get_object_or_404(CustomUser, rut=rut)
    usuario_actual = CustomUser.objects.get(rut=rut)
    correo_destinatario = usuario_actual.email
    print(correo_destinatario)
    
    # Generar el token para restablecer la contraseña
    token = default_token_generator.make_token(usuario_actual)
    # Crear la URL de restablecimiento de contraseña
    uidb64 = urlsafe_base64_encode(force_bytes(usuario_actual.pk))
    reset_url = f"http://127.0.0.1:8000/reset/{uidb64}/{token}/"
    # reset_url = reverse('restablecer_contrasenia', kwargs={'uidb64': uidb64, 'token': token})


    print(reset_url)

    

    # Obtenemos el template y renderizamos con el contexto
    context = {'usuario': usuario_actual, 'reset_url': reset_url}
    template = get_template('reset_password/prueba.html')
    content = template.render(context)
    
    correo = EmailMultiAlternatives(
        'Restaurar tu contraseña - Servicio de Salud Lebu',
        'Servicio de Salud',
        settings.EMAIL_HOST_USER,
        [correo_destinatario]
        # ['salvador0796@gmail.com']
    )
    correo.attach_alternative(content, 'text/html')
    correo.send()
    
def restablecer_contrasenia(request, uidb64, token):
    try:
        # Decodificar el uidb64 y obtener el usuario
        # user_id = force_text(urlsafe_base64_decode(uidb64))
        user_id = str(urlsafe_base64_decode(uidb64), 'utf-8')
        user = CustomUser.objects.get(pk=user_id)

        # Verificar que el token sea válido
        if default_token_generator.check_token(user, token):
            # Si el token es válido, permitir al usuario restablecer la contraseña
            # Aquí puedes redirigir a un formulario de restablecimiento de contraseña personalizado
            # o procesar el restablecimiento directamente en esta vista.
            
            if request.method == 'POST':
                nueva_contrasenia = request.POST.get('nueva-contrasenia', None)
                nueva_contrasenia_repetida = request.POST.get('nueva-contrasenia-repetida', None)
                
                if nueva_contrasenia == nueva_contrasenia_repetida:
                    user.set_password(nueva_contrasenia)   
                    user.save()
                    messages.success(request, 'Contraseña cambiada con exito')
                else:
                    messages.error(request, 'Las contraseñas no coinciden')
                

            # Ejemplo: redirigir a una vista de formulario de restablecimiento de contraseña
            return render(request, 'reset_password/nuevo_password.html', {'uidb64': uidb64, 'token': token})
        else:
            messages.error(request, 'El enlace de restablecimiento de contraseña es inválido.')
            return HttpResponse('El enlace de restablecimiento de contraseña es inválido.')
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        messages.error(request, 'El enlace de restablecimiento de contraseña es inválido.')
        return HttpResponse('El enlace de restablecimiento de contraseña es inválido.')    
    

def recuperar_contrasenia(request):
    if request.method == 'POST':
        rut = request.POST.get('rut', None)
        try:
            enviar_correo(rut)      
        except Exception as e:
            print(e)
    
    return render(request, 'reset_password/reset_por_rut.html')



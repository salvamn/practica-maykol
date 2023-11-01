from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def iniciar_sesion(request):
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


def recuperar_contrasenia(reques):
    pass
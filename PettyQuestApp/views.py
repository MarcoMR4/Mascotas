from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CrearUsuario, InicioSesion, RegistroForm, buscadorContactoMensajeria, enviarMensaje
from .models import Mascota
from django.contrib.auth.models import User 
from django.views.generic import CreateView
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


# Create your views here.

def index(request):
        if request.method == 'GET':
                title = 'Adopcion de mascotas'
                return render(request, 'index.html', {
                'title': title,
                'formUsuario': CrearUsuario,
                'formInicio' : InicioSesion 
                })
        else:   
                print("Entro al POST")
                Usuario.objects.create(nombre=request.POST['nombre'], apellidoP=request.POST['apellidoP'], apellidoM=request.POST['apellidoM'],fechaNacimiento=request.POST['fechaNacimiento'],correoElectronico=request.POST['correoElectronico'],contraseña=request.POST['contraseña1'],telefono=request.POST['telefono'],calle=request.POST['calle'],numero=request.POST['numero'],colonia=request.POST['colonia'],ciudad=request.POST['ciudad'],codigoPostal=request.POST['codigoPostal'])
                return redirect('index')
                

def catalogo(request):
    title = 'Catalogo de mascotas'
    return render(request , 'mascotas/catalogoMascotas.html',{
            'title' : title
    })

def registro(request):
        if request.method == 'GET':
                title = 'Registro de usuario'
                return render(request, 'usuario/registro.html', {
                'title': title,
                'formRegistro': RegistroForm,
                'formInicio' : InicioSesion 
                })
        else : 
                if request.POST['password1'] == request.POST['password2']:
                        try:
                                user = User.objects.create_user(
                                username=request.POST['username'],first_name=request.POST['first_name'] , last_name=request.POST['last_name'], password=request.POST['password1'], )
                                user.save()
                                login(request, user)
                                return redirect('index')
                        except IntegrityError:
                                return render(request, 'usuario/registro.html', {
                                'formRegistro': RegistroForm,
                                'formInicio' : InicioSesion,
                                'error2': 'Username already exist'
                                })
                else:
                        return render(request, 'usuario/registro.html', {
                                'formRegistro': RegistroForm,
                                'formInicio' : InicioSesion,
                                'error2': 'Password do not match'
                        })

def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method == 'GET':
        return render(request, 'usuario/inicioSesion.html', {
            'formInicio': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
             return render(request, 'usuario/inicioSesion.html', {
            'formInicio': AuthenticationForm,
            'error2': 'Username or password is incorrect'
             })
        else  :
             login(request, user)
             return redirect('index')   

def registromascota(request):
        if request.method == 'GET':
                 return render(request , 'mascotas/registroMascota.html',{
                'title' : "Registrar mascota"
    })
        else :
                print("Entro al POST")
                Mascota.objects.create(nombre=request.POST['masnombre'], genero=request.POST['genero'], tipo=request.POST['idRazaAnimal'],raza=request.POST['razamas'],personalidad=request.POST['personalidad'],edad=request.POST['edadmas'],tamaño=request.POST['tamano'],ubicacion=request.POST['ubicacion'],historial=request.POST['historial'],foto=request.POST['fotomas'],video=request.POST['video'])
      

def mensajes(request):
    title = 'Mensajes'
    return render(request , 'mensajeria/mensajes.html',{
            'title' : title,
            'formBuscar' : buscadorContactoMensajeria,
            'formEnviar': enviarMensaje
    }) 
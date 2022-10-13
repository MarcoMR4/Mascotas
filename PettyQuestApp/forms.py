from binascii import a2b_base64
from cProfile import label
from re import A
from django import forms
from pkg_resources import require
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 
            'username',         
                  
            'first_name',
            'last_name'
        ]
        labels ={
            'username' : 'Correo Electronico',
            
            'first_name' : 'Nombre:',
            'last_name' : 'Apellidos:',
            'numeroCasa' : 'Numero:',
            'colonia' : 'Colonia:',
            'ciudad' : 'Ciudad:',
            'codigoPostal' : 'Codigo postal:'
        }

class CrearUsuario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=45)
    apellidoP = forms.CharField(label="Apellido Paterno", max_length=45)
    apellidoM = forms.CharField(label="Apellido materno", max_length=45)
    fechaNacimiento = forms.CharField(label="Fecha de nacimiento")
    correoElectronico = forms.EmailField(label="Correo electronico", max_length=45)
    contraseña1 = forms.CharField(label="Contraseña", max_length=45, min_length=8)
    contraseña2 = forms.CharField(label="Confirmar contraseña", max_length=45, min_length=8)
    telefono = forms.CharField(label="Telefono", max_length=45)
    calle = forms.CharField(label="Calle", max_length=45)
    numero  = forms.CharField(label="Numero de casa", max_length=45)
    colonia = forms.CharField(label="Colonia", max_length=45)
    ciudad  = forms.CharField(label="Ciudad", max_length=45)
    codigoPostal = forms.CharField(label="Codigo postal", max_length=45)

class InicioSesion(forms.Form):
    correoElectronico = forms.EmailField(label="Correo electronico", max_length=45)
    contraseña = forms.CharField(label="Contraseña", max_length=45, min_length=8)


class buscadorContactoMensajeria(forms.Form):
    buscador = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'placeholder':'Nombre de contacto',
                'style':'resize:none;', 'rows':'1'
            }
        )
    )

class enviarMensaje(forms.Form):
    enviar = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'placeholder':'Escribe aquÃ­ tu mensaje',
                'style':'resize:none;', 'name':'mensajeContacto',
                'id':'mensajeContacto', 'rows':'1', 'cols':'10'
            }
        )
    )


from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('catalogo/', views.catalogo, name="catalogoMas"),
    path('registro/', views.registro, name="registro"),
    path('inicioSesion/', views.signin, name="inicioSesion"),
    path('logout/', views.signout, name='logout'),
    path('registroMascota/', views.registromascota, name="registroMascota"),
    path('mensajes/', views.mensajes, name="mensajes"),
    
]
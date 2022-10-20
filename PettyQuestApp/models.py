from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    Especie = models.ForeignKey('Especie', on_delete=models.CASCADE, null = True, blank = True)
    raza = models.CharField(max_length=200)
    personalidad = models.CharField(max_length=200)
    edad = models.CharField(max_length=200)
    tamaño = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    historial = models.TextField()
    foto = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    estatus = models.ForeignKey('Estatus', on_delete=models.CASCADE, null = True, blank = True)

    def Mostrar(self):
        return "{}".format(self.nombre)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Mascota'
        verbose_name_plural= 'Mascotas'
        db_table= 'Mascota'
        ordering= ['id']


class AsociacionVeterinaria(models.Model):
    nombreOrg = models.CharField(max_length=200)   
    ciudad = models.CharField(max_length=200)
    colonia = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    geolocalizaicion = models.CharField(max_length=200 , null = True, blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def Mostrar(self):
        return "{}".format(self.nombreOrg)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'AsociacionVeterinaria'
        verbose_name_plural= 'AsociacionesVeterinarias'
        db_table= 'AsociacionVeterinaria'
        ordering= ['id']


class Usuario (models.Model):
    edad = models.CharField(max_length=200)   
    ciudad = models.CharField(max_length=200)
    colonia = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    geolocalizaicion = models.CharField(max_length=200 , null = True, blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def Mostrar(self):
        return "{}".format(self.user)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Usuario'
        verbose_name_plural= 'Usuarios'
        db_table= 'Usuario'
        ordering= ['id']


class Especie(models.Model):
    nombre = models.CharField(max_length=200)

    def Mostrar(self):
        return "{}".format(self.nombre)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Especie'
        verbose_name_plural= 'Especies'
        db_table= 'Especie'
        ordering= ['id']


class Estatus(models.Model):
    nombre = models.CharField(max_length=200)

    def Mostrar(self):
        return "{}".format(self.nombre)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Estatus'
        verbose_name_plural= 'Estatus'
        db_table= 'Estatus'
        ordering= ['id']



class Mensaje(models.Model):
    mensaje = models.CharField(max_length=200)
    claveRemitente = models.CharField(max_length=200)
    claveDestinatario = models.CharField(max_length=200)
    usuario = models.SmallIntegerField()
    cartilla = models.CharField(max_length=200)
    mascota = models.CharField(max_length=200)
    visto = models.SmallIntegerField()

    def Mostrar(self):
        return "{} - {}".format(self.claveRemitente, self.claveDestinatario)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Mensaje'
        verbose_name_plural= 'Mensajes'
        db_table= 'Mensaje'
        ordering= ['id']


class contratoAdopcion(models.Model):
    comporbanteDomicilio = models.CharField(max_length=200)
    fecha = models.DateField(default=now)
    idUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null = True, blank = True)
    idMascota = models.ForeignKey('Mascota', on_delete=models.CASCADE, null = True, blank = True)
    idAsociacion = models.ForeignKey('AsociacionVeterinaria', on_delete=models.CASCADE, null = True, blank = True)
    ine = models.CharField(max_length=200)
    razones = models.CharField(max_length=1000)

    def Mostrar(self):
        return "{} - {}".format(self.idUsuario, self.idAsociacion)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'contratoAdopcion'
        verbose_name_plural= 'contratosAdopcion'
        db_table= 'contratoAdopcion'
        ordering= ['id']


class Notificacion(models.Model):
    fechaAnt = models.DateField()
    fechaActual = models.DateField(default=now)
    fechaSig = models.DateField()
    claveContrato = models.ForeignKey('contratoAdopcion', on_delete=models.CASCADE, null = True, blank = True)

    def Mostrar(self):
        return "{}".format(self.claveContrato)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Notificacion'
        verbose_name_plural= 'Notificaciones'
        db_table= 'Notificacion'
        ordering= ['id']
        
class fk_mascota_usuario(models.Model):
    claveMascota = models.ForeignKey('Mascota', on_delete=models.CASCADE, null = True, blank = True)
    idUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null = True, blank = True)

    def Mostrar(self):
        return "{} - {}".format(self.claveMascota, self.idUsuario)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'fk_mascota_usuario'
        verbose_name_plural= 'fk_mascota_usuario'
        db_table= 'fk_mascota_usuario'
        ordering= ['id']
    

class fk_contrato_mascota(models.Model):
    claveMascota = models.ForeignKey('Mascota', on_delete=models.CASCADE, null = True, blank = True)
    claveContrato = models.ForeignKey('contratoAdopcion', on_delete=models.CASCADE, null = True, blank = True)

    def Mostrar(self):
        return "{} - {}".format(self.claveMascota, self.claveContrato)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'fk_contrato_mascota'
        verbose_name_plural= 'fk_contrato_mascota'
        db_table= 'fk_contrato_mascota'
        ordering= ['id']


class fk_contrato_asociacionveterinaria(models.Model):
    claveAsociacionVeterinaria = models.ForeignKey('AsociacionVeterinaria', on_delete=models.CASCADE, null = True, blank = True)
    claveContrato = models.ForeignKey('contratoAdopcion', on_delete=models.CASCADE, null = True, blank = True)

    def Mostrar(self):
        return "{} - {}".format(self.claveAsociacionVeterinaria, self.claveContrato)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'fk_contrato_asociacionveterinaria'
        verbose_name_plural= 'fk_contrato_asociacionveterinaria'
        db_table= 'fk_contrato_asociacionveterinaria'
        ordering= ['id']


class fk_mascota_asociacionveterinaria(models.Model):
    claveMascota = models.ForeignKey('Mascota', on_delete=models.CASCADE, null = True, blank = True)
    claveAsociacionVeterinaria = models.ForeignKey('AsociacionVeterinaria', on_delete=models.CASCADE, null = True, blank = True)

    def Mostrar(self):
        return "{} - {}".format(self.claveMascota, self.idUsuario)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'fk_mascota_asociacionveterinaria'
        verbose_name_plural= 'fk_mascota_asociacionveterinaria'
        db_table= 'fk_mascota_asociacionveterinaria'
        ordering= ['id']


class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def Mostrar(self):
        return "{}".format(self.user)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Administrador'
        verbose_name_plural= 'Administradores'
        db_table= 'Administrador'
        ordering= ['id']
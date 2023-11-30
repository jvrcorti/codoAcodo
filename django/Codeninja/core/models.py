from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUsuario(AbstractUser):
    name = models.CharField(max_length=30, verbose_name='Nombre de Usuario')
    username = models.CharField(
        max_length=30, unique=True, verbose_name='Nombre de logueo')
    email = models.EmailField(max_length=50, verbose_name='Email')
    groups = models.ManyToManyField(
        Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='custom_user_set', blank=True)

    def __str__(self):
        return self.username

# Formulario asociado al modelo


class MiConsulta(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nombre y Apellido')
    email = models.EmailField(max_length=50, verbose_name='Email')
    consulta = models.TextField(verbose_name='Consulta', null=True)
    # Relacion muchos a muchos
    relacion_servicio = models.ManyToManyField(
        'Service', through='ConsultaServicio', related_name='consultas_relacionadas')

    def __str__(self):
        return self.name

# Relaciones uno a muchos


class ConsultaServicio(models.Model):
    consuta = models.ForeignKey(MiConsulta, on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)


class Service(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Nombre del servicio',
    )
    description = models.CharField(
        max_length=30, verbose_name='Descripción del servicio')
    package = models.CharField(
        max_length=30, verbose_name='Actualizaciones del servicio')
    support = models.CharField(
        max_length=2, verbose_name='Desarrollo con asistencia virtual')

    def __str__(self):
        return self.name

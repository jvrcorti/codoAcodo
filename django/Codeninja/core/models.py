from django.db import models


class MiConsulta(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nombre y Apellido')
    email = models.EmailField(max_length=50, verbose_name='Email')
    consulta = models.TextField(verbose_name='Consulta', null=True)

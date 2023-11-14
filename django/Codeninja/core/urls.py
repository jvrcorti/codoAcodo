from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('servicios/', views.servicios, name='servicios'),
    # ==> Url de la vista parametrizada <== #
    re_path('servicios/<int:servicio_id>/',
            views.servicios_detail, name='detalle_servicio'),
    path('proyectos/', views.proyectos, name='proyectos'),
]

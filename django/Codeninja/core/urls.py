from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views
from .views import PaginaLoginView, CustomUsuarioView


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login',
         auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    # path('accounts/login', PaginaLoginView.as_view(), name='login'),
    # ==> URL de la vista en clase <==
    path('servicios/', views.ServiceListView.as_view(), name='servicios'),
    #    path('servicios/', views.servicios, name='servicios'),
    # ==> Url de la vista parametrizada <== #
    re_path('servicios/<int:servicio_id>/',
            views.servicios_detail, name='detalle_servicio'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('registro/', CustomUsuarioView.as_view(), name='registro')
]

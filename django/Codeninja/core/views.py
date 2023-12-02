from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .forms import ContactoForms
from .models import Service, MiConsulta
import datetime


class PaginaLoginView(LoginView):
    template_name = 'core/login.html'
    success_url = reverse_lazy('core/servicios.html')

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(
            self.request, form.error_messages['Sos  boludo. Pone bien la contraseña'])
        return response


class CustomUsuarioView(CreateView):
    template_name = 'core/registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('core/login.html')

# ==> Formulario asociado a template y basado en clase a través forms.py <== #
# ==> Validacón del backend. Para ver debe estar autenticado <==


@login_required
def index(request):
    if request.method == 'POST':
        form = ContactoForms(request.POST)
        if form.is_valid():
            consulta = form.save()
            print(form.cleaned_data)
            return redirect('index')
    else:
        form = ContactoForms()

    return render(request, 'core/index.html', {'form': form})

# ==> Vista basada en clase <==


class ServiceListView(ListView):
    model = Service
    context_object_name = 'servicios'
    template_name = 'core/servicios.html'
    ordering = ['name']
#    def servicios(request):
#    return render(request, 'core/servicios.html')


# ==> Vista parametrizada <== #
def servicios_detail(request, servicio_id):
    return HttpResponse(f'Detalle del servicio con ID: {servicio_id}')


def proyectos(request):
    return render(request, 'core/proyectos.html')


def mostrar_consulta(request):
    datos = MiConsulta.objects.all()
    return render(request, 'login.html', {'datos': datos})

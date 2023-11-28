from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from .forms import ContactoForms
import datetime

# ==> Formulario asociado a template y basado en clase a través forms.py <== #


def index(request):
    context = {'fecha_actual': datetime.datetime.now()}
    if request.method == 'POST':
        form = ContactoForms(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('servicios')
    else:
        form = ContactoForms()
    return render(request, 'core/index.html', {'form': form})


def servicios(request):
    return render(request, 'core/servicios.html')


# ==> Vista parametrizada <== #
def servicios_detail(request, servicio_id):
    return HttpResponse(f'Detalle del servicio con ID: {servicio_id}')


def proyectos(request):
    return render(request, 'core/proyectos.html')

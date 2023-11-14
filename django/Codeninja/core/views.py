from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactoForms


# ==> Formulario asociado a template y basado en clase forms.py <== #
def index(request):
    if request.method == 'POST':
        form = ContactoForms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ContactoForms()
    return render(request, 'core/index.html', {'form': form})


def servicios(request):
    return render(request, 'core/servicios.html')


# Vista parametrizada#
def servicios_detail(request, servicio_id):
    return HttpResponse(f'Detalle del servicio con ID: {servicio_id}')


def proyectos(request):
    return render(request, 'core/proyectos.html')

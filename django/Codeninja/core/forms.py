from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from .models import MiConsulta, Service
import re


class UserAuthenticationForm(AuthenticationForm):
    error_massages = {
        'invalid_login': 'Sos boludo, logueate bien querés',
        'inactive': 'Esta cuenta está inactiva',
    }
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'autofocus': True}),
    )

# ==> Formulario basado en clase <==


class ContactoForms(forms.ModelForm):
    class Meta:
        model = MiConsulta
        fields = ["name", "email", "consulta", "relacion_servicio"]

        name = forms.CharField(label='Nombre y Apellido', required=True, widget=forms.TextInput(
            attrs={'placeholder': 'Ingrese su nombre y apellido'})),
        email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(
            attrs={'placeholder': 'Ingresa tu correo electrónico'})),
        consulta = forms.CharField(label='Consúltanos', required=True, widget=forms.Textarea(
            attrs={'placeholder': 'Ingrese su consulta', 'class': 'consulta'})),

        relacion_servicio = forms.ModelMultipleChoiceField(
            queryset=Service.objects.all(), widget=forms.CheckboxSelectMultiple)

    # ==> Realiza validacion sobre los campos del formulario, todos son obligatorios <== #

    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if re.search(r'\d', name):
            raise forms.ValidationError('Ingrese su Nombre y Apellido.')
        # ==>Validamos en la base de datos si el nombre ya existe. <==
        elif MiConsulta.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
            self.add_error(
                'name', 'El Nombre y Apellido ya esta inscripto en nuestras bases.')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not forms.EmailField:
            raise forms.ValidationError('Ingrese su email de contacto')
        # ==> Validamos en la base de datos si el email ya existe. <==
        elif MiConsulta.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            self.add_error(
                'email', 'Esta cuenta de e-mail ya se encuetra registrado.')
        return email

    def clean_consulta(self):
        consulta = self.cleaned_data.get('consulta')
        if len(consulta.strip()) < 10:  # strip(): quita los espacios del principio y final
            raise forms.ValidationError(
                'Ingrese su consulta sobre nuestros servicios.')
        return consulta

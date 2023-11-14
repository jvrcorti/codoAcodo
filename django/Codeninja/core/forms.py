from django import forms
from django.core.exceptions import ValidationError
import re


class ContactoForms(forms.Form):
    name = forms.CharField(label='Nombre y Apellido', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ingrese su nombre y apellido'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ingresa tu correo electrónico'}))
    consulta = forms.CharField(label='Consúltanos', required=True, widget=forms.Textarea(
        attrs={'placeholder': 'Ingrese su consulta', 'class': 'consulta'}))

# Realiza validacion sobre los campos del formulario, todos son obligatorios
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if re.search(r'\d', name):
            raise forms.ValidationError('Ingrese su Nombre y Apellido.')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not forms.EmailField:
            raise forms.ValidationError('Ingrese su email de contacto')
        return email

    def clean_consulta(self):
        consulta = self.cleaned_data.get('consulta')
        if len(consulta) < 10:
            raise forms.ValidationError(
                'Ingrese su consulta sobre nuestros servicios.')
        return consulta

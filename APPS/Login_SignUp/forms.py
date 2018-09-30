# -*- coding: utf-8 -*-
from django import forms
from .models import *


class SolicitanteForm(forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ['Nombre', 'Apellido', 'Sexo', 'Fecha_Nacimiento', 'Cedula', 'Email', 'Clave', 'Clave2', 'Estado']
        """labels = {
                        'Cedula': 'Cédula',
                        'Nombre': 'Nombre',
                        'Apellido': 'Apellido',
                        'Sexo': 'Sexo',
                        'Fecha_Nacimiento': 'Fecha de Nacimiento',
                        'Email': 'Email',
                        'Clave': 'Contraseña',
                        'Estado': 'Estado'
                        }"""

        widgets = {
            'Nombre': forms.TextInput(attrs={
                'id': "nombre",
                'class': "form-control",
                'type': "text",
                'placeholder': "Nombre",
                'name': "nombre",
                'title': "Ingrese su nombre"
            }),

            'Apellido': forms.TextInput(attrs={
                'id': "apellido",
                'class': "form-control",
                'type': "text",
                'placeholder': "Apellido",
                'name': "apellido",
                'title': "Ingrese su apellido.",
            }),

            'Sexo': forms.Select(attrs={
                'name': "genero",
                'id': "genero",
                'class': "form-control Genero",
                'required': "required",
                'title': "Seleccione el genero correspondiente"
            }),

            'Fecha_Nacimiento': forms.DateInput(attrs={
                'type': "date",
                'name': "date",
                'id': "fechaNaci",
                'class': "form-control",
                'required': "required",
                'title': "Ingrese su fecha de nacimiento."
            }),

            'Cedula': forms.NumberInput(attrs={
                'class': "form-control",
                'type': "number",
                'name': "",
                'value': "",
                'required': "required",
                'placeholder': "Cedula de Indentidad",
                'id': "cedula"
            }),

            'Email': forms.EmailInput(attrs={
                'id': "email",
                'class': "form-control",
                'type': "email",
                'placeholder': "Email",
                'name': "email",
                'required': "required",
                'title': "Ingrese su email.",
                'style': "width: 47%; float: right;"
            }),

            'Clave': forms.PasswordInput(attrs={
                'id': "password",
                'class': "form-control",
                'type': "password",
                'placeholder': "Password",
                'name': "password",
                'title': "Ingrese un password.",
                'required': "required"
            }),

            'Clave2': forms.PasswordInput(attrs={
                'id': "password_confirmation",
                'class': "form-control",
                'type': "password",
                'placeholder': "Confirme su Password",
                'name': "password_confirmation",
                'title': "Confirme su password.",
                'required': "required"
            }),

            'Estado': forms.TextInput(attrs={
                'value': 'A',
                'style': 'display: none',
                'type': "text",
                'class': "form-control",
                'id': "Estado",
            })
        }


class EmpleadoresForm(forms.ModelForm):
    class Meta:
        model = Empleadores
        fields = ['Nombre', 'FechaConst', 'FormaJurd', 'RNC', 'Direccion', 'Email', 'Clave', 'Clave2', 'Estado']
        """labels = {
                'RNC': 'RNC',
                'Nombre': 'Nombre',
                'FechaConst': 'FechaConst',
                'FormaJurd': 'FormaJurd',
                'Email': 'Email',
                'Direccion': 'Direccion',
                'Clave': 'Clave',
                'Estado': 'Estado'
                }"""
        widgets = {
            'Nombre': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'nomEmpresa',
                'placeholder': 'Nombre de la Empresa',
                'title': 'Ingrese el nombre de la empresa.',
            }),

            'FechaConst': forms.DateInput(attrs={
                'type': 'date',
                'name': "fechaEmpresa",
                'id': "inputFechaEmpresa",
                'class': "form-control",
                'value': "",
                'required': "required",
                'title': "Ingrese la fecha de constitucion de la empresa."
            }),

            'FormaJurd': forms.Select(attrs={
                'name': "tipoEmpresa",
                'id': "inputTipoEmpresa",
                'class': "form-control",
                'required': "required",
                'title': "Seleccione el tipo de empresa correspondiente."
            }),

            'RNC': forms.NumberInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "RNC",
                'placeholder': "RNC de la empresa",
                'title': "Ingrese RNC de la empresa.",
            }),
            'Direccion': forms.Select(attrs={
                'type': "text",
                'class': "form-control",
                'id': "direccion",
                'placeholder': 'Direccion de la empresa',
                'title': "Ingrese la direccion de la empresa.",
                'style': 'width: 47%; float: left;'
            }),

            'Email': forms.EmailInput(attrs={
                'id': "email",
                'class': "form-control",
                'type': "email",
                'placeholder': "Email",
                'name': "emailEmpresa",
                'required': "required",
                'title': "Ingrese el email de la empresa."
            }),

            'Clave': forms.PasswordInput(attrs={
                'id': "password",
                'class': "form-control",
                'type': "password",
                'placeholder': "Password",
                'name': "password",
                'title': "Ingrese una password.",
                'required': "required"
            }),

            'Clave2': forms.PasswordInput(attrs={
                'id': "password_confirmation",
                'class': "form-control",
                'type': "password",
                'placeholder': "Confirme su Password",
                'name': "password_confirmation",
                'title': "Confirme su password.",
                'required': "required"
            }),

            'Estado': forms.TextInput(attrs={
                'value': 'A',
                'style': 'display: none',
                'type': "text",
                'class': "form-control",
                'id': "Estado",
            })

        }


class LoginForm(forms.Form):
    class Meta:
        correo = forms.CharField()
        clave = forms.CharField(widget=forms.PasswordInput())
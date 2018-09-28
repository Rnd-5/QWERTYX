# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from .forms import LoginForm
from django.contrib.auth import authenticate, login

import mongoengine
from pymongo.auth import authenticate
"""
user = authenticate(username='Rond', password='R0nd1998Mongo1005')
assert isinstance(user, mongoengine.django.auth.User)
"""
from APPS.Login_SignUp.forms import SolicitanteForm, EmpleadoresForm



def Log(request):
    if request.method == 'POST':
        form1 = SolicitanteForm(request.POST or None)
        form2 = EmpleadoresForm(request.POST or None)
        if form1.is_valid():
            #if form1.
            form1.save()
            return redirect('Log')
        if form2.is_valid():
            form2.save()
            return redirect('Log')
    else:
        form1 = SolicitanteForm()
        form2 = EmpleadoresForm()
    return render(request, 'Login_Registro.html', {'form_Solct': form1, 'form_Empl': form2})


def home(request):
    return render(request, 'home.html', {})

def log_page(request):
    message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user.is_active:
                login(request, user)
                message = "Te has identificado de manera correcta."
            else:
                message = "Tu usuario esta inactivo."
        else:
            message = "Nombre o password incorrecto."
    else:
        form = LoginForm()
    return render_to_response('Login_Registro.html', {'message': message, 'form': form})
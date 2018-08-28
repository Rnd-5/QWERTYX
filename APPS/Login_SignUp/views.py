# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

import mongoengine
from pymongo.auth import authenticate
"""
user = authenticate(username='Rond', password='R0nd1998Mongo1005')
assert isinstance(user, mongoengine.django.auth.User)
"""
from APPS.Login_SignUp.forms import SolicitanteForm, EmpleadoresForm


# Create your views here.


def Log(request):
    if request.method == 'POST':
        form1 = SolicitanteForm(request.POST or None)
        form2 = EmpleadoresForm(request.POST or None)
        if form1.is_valid():
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

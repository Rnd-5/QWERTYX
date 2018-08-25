# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import mongoengine
from pymongo.auth import authenticate

user = authenticate(username='Rond', password='R0nd1998Mongo1005')
assert isinstance(user, mongoengine.django.auth.User)

# Create your views here.

def Log(request):
    if request.method == 'POST':
        form1 = SolicitanteForm(request.POST)
        form2 = EmpleadoresForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('App_Get_a_Job:Log')
        if form2.is_valid():
            form2.save()
            return redirect('App_Get_a_Job:Log')
    else:
        form1 = SolicitanteForm()
        form2 = EmpleadoresForm()
    return render(request, 'crearEmpl2.html', {'form_Solct': form1, 'form_Empl': form2})

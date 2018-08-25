# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mongoengine import *
from GET_A_JOB_Proyecto_1.settings import BDNAME
# Create your models here.

connect(BDNAME)


class Genero(models.Model):
    Cod_Gen = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=20)
    Sigla = models.CharField(max_length=1)

    def __str__(self):
        return self.Sigla

class Solicitante(models.Model):
    Cedula = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=100)
    Sexo = models.ForeignKey(Genero, on_delete=models.CASCADE)
    Fecha_Nacimiento = models.DateField()
    Email = models.EmailField(max_length=50)
    Clave = models.CharField(max_length=75)
    Clave2 = models.CharField(max_length=75)
    Estado = models.CharField(max_length=1)

    def __str__(self):
        return self.Nombre + " " + self.Apellido

class TipoEmpresa(models.Model):
    Cod_TipoEmpr = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=10)
    Descripcion = models.CharField(max_length=60)

    def __str__(self):
        return self.Nombre

class Provincias(models.Model):
    Cod_Provincia = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Empleadores(models.Model):
    Nombre = models.CharField(max_length=50)
    FechaConst = models.DateField()
    FormaJurd = models.ForeignKey(TipoEmpresa, on_delete=models.CASCADE)
    RNC = models.IntegerField(primary_key=True)
    Direccion = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    Email = models.EmailField(max_length=50)
    Clave = models.CharField(max_length=75)
    Clave2 = models.CharField(max_length=75)
    Estado = models.CharField(max_length=1)

    def __str__(self):
        return self.Nombre + " " + str(self.FormaJurd)


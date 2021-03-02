from django.shortcuts import render
from Database.models import User, Locations
from django.http import HttpResponse

# Create your views here.

def mostrar(request):
    userin=User.objects.get(first_name="Andres")
    return HttpResponse("El usuario {} que vive en {} fue creado exitosamente".format(userin.first_name, userin.location_id.name))
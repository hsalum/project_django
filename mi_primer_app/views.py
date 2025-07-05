from django.shortcuts import render
from .models import Familia

# Create your views here.
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡Hola Mundo!")

def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')

def crear_familiar(request, nombre):
    if nombre is not None:
        nuevo_familiar = Familia(nombre=nombre, apellido="Apellido", edad=30, fecha_nacimiento="1993-01-01", parentesco="Primo")
        nuevo_familiar.save()
    return HttpResponse(f"Familiar {nombre} creado exitosamente.")
def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'mi_primer_app/profesores.html', {'profesores': profesores})
from django.shortcuts import render,redirect
from .models import Familia, Curso, Estudiante, Profesor
from .forms import cursoForm, EstudianteForms, ProfesorForm
def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                especialidad=form.cleaned_data['especialidad'],
                curso=form.cleaned_data['curso']
            )
            profesor.save()
            return redirect('profesores')
    else:
        form = ProfesorForm()
    return render(request, 'mi_primer_app/crear_profesor.html', {'form': form})

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')

def saludo(request):
    return HttpResponse("¡Hola Mundo!")

def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')

def crear_familiar(request, nombre):
    if nombre is not None:
        nuevo_familiar = Familia(nombre=nombre, apellido="Apellido", edad=30, fecha_nacimiento="1993-01-01", parentesco="Primo")
        nuevo_familiar.save()
    return HttpResponse(f"Familiar {nombre} creado exitosamente.")

def crear_curso(request):
    if request.method == 'POST':
        form = cursoForm(request.POST)
        if form.is_valid():
            nuevo_curso = Curso(
                nombre = form.cleaned_data['nombre'],
                descripcion = form.cleaned_data['descripcion'],
                duracion_semanas = form.cleaned_data['duracion_semanas'],
                fecha_inicio = form.cleaned_data['fecha_inicio'],
                activo = form.cleaned_data['activo']
            )
            nuevo_curso.save()
            return redirect('cursos')
    else:
        form = cursoForm()
    return render(request, 'mi_primer_app/crear_curso.html', {'form': form})


def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForms(request.POST)
        if form.is_valid():
            nuevo_estudiante = Estudiante(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                email = form.cleaned_data['email'],
                edad = form.cleaned_data['edad'],
                fecha_inscripcion = form.cleaned_data['fecha_inscripcion']
            )
            nuevo_estudiante.save()
            return redirect('inicio')
    else:
        form = EstudianteForms()
    return render(request, 'mi_primer_app/crear_estudiante.html', {'form': form})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos})

def buscar_cursos(request):
    if request.method == 'GET':
        nombre_curso = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
        return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos, 'nombre_curso': nombre_curso})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Familia, Curso, Estudiante, Profesor
from .forms import cursoForm, EstudianteForms, ProfesorForm, FamiliarForm


def profesores(request):
    profesores = Profesor.objects.all()
    mensaje_exito = request.session.pop('mensaje_exito', None)
    return render(request, 'mi_primer_app/profesores.html', {'profesores': profesores, 'mensaje_exito': mensaje_exito})

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
            request.session['mensaje_exito'] = f"Profesor {profesor.nombre} {profesor.apellido} creado exitosamente."
            return redirect('profesores')
    else:
        form = ProfesorForm()
    return render(request, 'mi_primer_app/crear_profesor.html', {'form': form})

def inicio(request):
    mensaje_exito = request.session.pop('mensaje_exito', None)
    return render(request, 'mi_primer_app/inicio.html', {'mensaje_exito': mensaje_exito})

def saludo(request):
    return HttpResponse("¡Hola Mundo!")

def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')

def crear_familiar(request):
    if request.method == 'POST':
        form = FamiliarForm(request.POST)
        if form.is_valid():
            nuevo_familiar = Familia(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                edad=form.cleaned_data['edad'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                parentesco=form.cleaned_data['parentesco']
            )
            nuevo_familiar.save()
            request.session['mensaje_exito'] = f"Familiar {nuevo_familiar.nombre} {nuevo_familiar.apellido} creado exitosamente."
            return redirect('familiares')
    else:
        form = FamiliarForm()
    return render(request, 'mi_primer_app/crear_familiar.html', {'form': form})

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
            request.session['mensaje_exito'] = f"Curso '{nuevo_curso.nombre}' creado exitosamente."
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
            request.session['mensaje_exito'] = f"Estudiante {nuevo_estudiante.nombre} {nuevo_estudiante.apellido} creado exitosamente."
            return redirect('estudiantes')
    else:
        form = EstudianteForms()
    return render(request, 'mi_primer_app/crear_estudiante.html', {'form': form})

def cursos(request):
    cursos = Curso.objects.all()
    mensaje_exito = request.session.pop('mensaje_exito', None)
    return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos, 'mensaje_exito': mensaje_exito})

def buscar_cursos(request):
    if request.method == 'GET':
        nombre_curso = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
        return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos, 'nombre_curso': nombre_curso})

def familiares(request):
    familiares = Familia.objects.all()
    mensaje_exito = request.session.pop('mensaje_exito', None)
    return render(request, 'mi_primer_app/familiares.html', {'familiares': familiares, 'mensaje_exito': mensaje_exito})

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    mensaje_exito = request.session.pop('mensaje_exito', None)
    return render(request, 'mi_primer_app/estudiantes.html', {'estudiantes': estudiantes, 'mensaje_exito': mensaje_exito})
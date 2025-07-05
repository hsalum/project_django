from django.urls import path

from mi_primer_app.views import saludo, saludo_con_template, crear_familiar, inicio, crear_curso, crear_estudiante, cursos, buscar_cursos, crear_profesor, profesores, familiares, estudiantes

urlpatterns = [
    path('', inicio, name='inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/', crear_familiar, name='crear_familiar'),
    path('crear-curso/', crear_curso, name='crear_curso'),
    path('crear-estudiante/', crear_estudiante, name='crear_estudiante'),
    path('cursos/',cursos, name='cursos'),
    path('cursos-buscar', buscar_cursos, name='buscar_cursos'),
    path('crear-profesor/', crear_profesor, name='crear_profesor'),
    path('profesores/', profesores, name='profesores'),
    path('familiares/', familiares, name='familiares'),
    path('estudiantes/', estudiantes, name='estudiantes'),
]


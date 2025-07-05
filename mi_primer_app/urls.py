

from django.urls import path
from mi_primer_app.views import saludo, saludo_con_template, crear_familiar

urlpatterns = [
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/<str:nombre>/', crear_familiar),
]


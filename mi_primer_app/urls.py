from django.urls import path
from mi_primer_app.views import saludo

urlpatterns = [
    path('hola-mundo/', saludo),
]

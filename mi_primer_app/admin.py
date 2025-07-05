from django.contrib import admin

# Register your models here.
from .models import Familia, Curso, Estudiante

register_models = [Familia, Curso, Estudiante]

admin.site.register(register_models)

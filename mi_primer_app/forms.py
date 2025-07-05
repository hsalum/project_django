from django import forms

class cursoForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea, required=False, label='Descripción')
    duracion_semanas = forms.IntegerField(min_value=1, initial=4, label='Duración (semanas)')
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2031)), label='Fecha de Inicio')
    activo = forms.BooleanField(required=False, initial=True, label='Activo')  


class EstudianteForms(forms.Form):
    nombre = forms.CharField(max_length=50, label='Nombre')
    apellido = forms.CharField(max_length=50, label='Apellido')
    email = forms.EmailField(label='Email', required=False)
    edad = forms.IntegerField(min_value=0, label='Edad')
    fecha_inscripcion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
   
  
class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50, label='Nombre')
    apellido = forms.CharField(max_length=50, label='Apellido')
    email = forms.EmailField(label='Email')
    especialidad = forms.CharField(max_length=100, label='Especialidad')
    curso = forms.CharField(max_length=100, label='Curso que dicta')

class FamiliarForm(forms.Form):
    nombre = forms.CharField(max_length=50, label='Nombre')
    apellido = forms.CharField(max_length=50, label='Apellido')
    edad = forms.IntegerField(min_value=0, label='Edad')
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de Nacimiento')
    parentesco = forms.CharField(max_length=50, label='Parentesco')
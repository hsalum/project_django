# Proyecto Django: ejemplo_django

Este proyecto es una aplicacion web desarrollada con Django que permite gestionar informacion de cursos, estudiantes, profesores y familiares.

## Funcionalidades principales

- **Página de inicio**: Vista inicial de la Web

- **Gestión de Cursos**:
  - Listar todos los cursos.
  - Crear nuevos cursos.
  - Buscar cursos por nombre.

- **Gestión de Estudiantes**:
  - Listar todos los estudiantes.
  - Crear nuevos estudiantes.

- **Gestión de Profesores**:
  - Listar todos los profesores.
  - Crear nuevos profesores.

- **Gestión de Familiares**:
  - Listar todos los familiares.
  - Crear nuevos familiares.

- **Saludo simple**: Pagina de saludo y ejemplo visto en clase.

## Funcionalidades Extras
- **Botones**: Al finalizar la creacion de Cualquier registro, podremos observar 2 Botones, uno para redireccionarnos al Inicio y otro para redireccionarnos a la Creacion de un nuevo registro.

## Modelos principales
- **Curso**: nombre, descripción, duración, fecha de inicio, estado.
- **Estudiante**: nombre, apellido, email, edad, fecha de inscripción.
- **Profesor**: nombre, apellido, email, especialidad, curso.
- **Familia**: nombre, apellido, edad, fecha de nacimiento, parentesco.


## Estructura de carpetas
- `mi_primer_app/`: Contiene la lógica de la aplicación (modelos, vistas, formularios, templates).
- `templates/`: Plantillas HTML.
- `requirements.txt`: Depenencias del proyecto.





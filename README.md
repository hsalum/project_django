# Proyecto Django: ejemplo_django

Este proyecto es una aplicacion web desarrollada con Django que permite gestionar informacion de cursos, estudiantes, profesores, familiares y mas!

## Funcionalidades principales

- **Página de inicio**: Vista principal de la aplicacion.

- **About**:
  - Informacion Acerca del Autor del proyecto.

- **Gestión de Cursos**:
  - Listar todos los cursos.
  - Crear nuevos cursos.
  - Buscar cursos por nombre.

- **Gestión de Profesores**:
  - Listar todos los profesores y los cursos que dictan.
  - Crear nuevos profesores.

- **Gestión de Estudiantes**:
  - Listar todos los estudiantes.
  - Crear nuevos estudiantes.
  
- **Gestión de Familiares**:
  - Listar todos los familiares.
  - Crear nuevos familiares.

- **Recomendaciones**:
  - Listar Computadoras cuyos componentes cumplan con los requisitos basicos para los cursos.
  - Crear nuevos registros de computadoras.
  - Editar Registros existentes.
  - Eliminar Registros.

- **Gestion de Usuario**: 
- En la plataforma podremos generarnos un usuario, el mismo cuenta con determinados permisos que permiten acceder a funcionalidades como Crear/editar/eliminar todo tipo de registro.
- Login & Logout 


## Cómo ejecutar el proyecto
1. Clonar el repositorio  
2. Crear y activar un entorno virtual  
3. Instalar las dependencias con:

    ```bash
    pip install -r requirements.txt
    ```

4. Ejecutar migraciones:

    ```bash
    python manage.py migrate
    ```

5. Ejecutar el servidor:

    ```bash
    python manage.py runserver
    ```

6. Acceder a `http://localhost:8000`


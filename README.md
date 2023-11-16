## EFI-PYTHON-DEVOPS

- Este proyecto consiste en un dockerizar una API de Flask donde se pueden gestionar usuarios, posteos, categorias y comentarios en un miniblog.
Este proyecto está disponible en https://github.com/ramiroquiro17/EFI_DevOps_Python.git" 

## Estructura del Proyecto

- *app*: Directorio principal de la aplicación.
  - *models.py*: Define los modelos de la base de datos.
  - *schemas.py*: Esquemas para la serialización de obtejos solicitados a la base de datos.
  - *templates.py*: Contiene el index.html, los demás templates no fueron implementados en este proyecto.
  - *views.py*: Define los endpoints o vistas de la aplicación.

- *migrations*: Contiene archivos relacionados con las migraciones de la base de datos.
- *.env.sample*: Ejemplo de configuración de las variables de entorno.
- *docker-compose.yml*: Define y configura los servicios de Docker.
- *Dockerfile*: Instrucciones para construir la imagen Docker de la aplicación.

- *README.md*: Descripción e implementación del proyecto.
- *requirements.txt*: Lista de dependencias del proyecto
- *run.sh*: Ejecuta las migraciones de base de datos e inicia la aplicación Flask utilizando un servidor WSGI como Gunicorn.

### Configuración del proyecto:

  **1- Crear un directorio para el proyecto y clonar el repositorio:** 

  git clone https://github.com/ramiroquiro17/EFI_DevOps_Python.git

  **2- Construir las imagenes y levantar los contenedores:**

  Crea y cofigura el archivo .env en base al archivo .env.sample según tus necesidades.

  **3- Construir las imagenes y levantar los contenedores:**

  docker-compose build && docker-compose up -d

  **4- Actualización de las migraciones:**

  flask db upgrade

  **Implementación de la API**

  Endpoints con MethodView:

  - Las vistas utilizan la clase MethodView de Flask. Se define una clase para
  cada modelo (User, Post, Comment, Category) que heredan de MethodView y
  utilizan los métodos (GET, POST, PUT, DELETE) para manejar las operaciones CRUD.

# Requisitos

Conocimientos previos de python y flask.

Manejo de docker.

Instalar programas:

docker: https://www.docker.com/get-started/

administrador base de datos: dbeaver(https://dbeaver.io/download/), sqlyog(https://sqlyog.es.download.it/)


## Solución de problemas

Si se te genera un error a la hora de subir información o modificar información y no sabes cual es el problema, asegúrese de:

- Tener la opción correcta al lado de la barra de búsqueda dependiendo de la función que deseas reaizar (POST, GET, PUT o DELETE).

- Asegurar que el enlace o puerto estén bien escritos. Ejemplo: localhost/5000:user/3

- Revisar que el tipo de texto sea JSON

- Separar cada columna con una coma

- Asegurar que el nombre de cada columna coincida con los nombres establecidos en el archivo views.

- Tener corriendo el comando flask run --reload

# Contribuyentes

- Matias Venencia
- m.venencia@itecriocuarto.org.ar

- Ramiro Quiroga
- r.quiroga@itecriocuarto.org.ar

- Luciano Avendaño
- l.avendano@itecriocuarto.org.ar


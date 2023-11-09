## EFI-PYTHON-DEVOPS

- Este proyecto consiste en una API donde se pueden ingresar datos relacionados al miniblog realizado en el primer semestre.

- Pueden filtrar el tipo de publicaciones que deseen observar a través de la opción categorías donde los usuarios pueden elegir o escribir el tipo de temática que desean encontrar en las públicaciones que le aparezcan al principio.

- Los nombres de usuarios no deben repetirse y en caso de que uno trate de registrarse con un nombre ya existente, se le aparecerá una alerta especificando que debe ingresar otro nombre.

- En las publicaciones y comentarios se podrá obtener el nombre del usuario que lo realizó y la fecha de creación.

- Todos los datos que se ingresen serán almacenados en una base de datos donde los administradores podrán observar de manera más organizada la nueva información y/o últimas ediciones de (publicaciones y comentarios) realizadas por usuarios, como también eliminar o realizar modificaciones en caso de ocnsiderarlo necesario.

## Contribuyentes

- Matias Venencia
- m.venencia@itecriocuarto.org.ar

- Ramiro Quiroga
- Gmail: r.quiroga@itecriocuarto.org.ar

- Luciano Avendaño ()
- Gmail: l.avendano@itecriocuarto.org.ar

## Requisitos

- Para correr esta aplicación se necesita tener instalado las siguientes librerías:

alembic==1.12.1
blinker==1.7.0
click==8.1.7
colorama==0.4.6
Flask==3.0.0
flask-marshmallow==0.15.0
Flask-Migrate==4.0.5
Flask-SQLAlchemy==3.1.1
greenlet==3.0.1
gunicorn==21.2.0
itsdangerous==2.1.2
Jinja2==3.1.2
load-dotenv==0.1.0
Mako==1.2.4
MarkupSafe==2.1.3
marshmallow==3.20.1
marshmallow-sqlalchemy==0.29.0
packaging==23.2
PyMySQL==1.1.0
python-dotenv==1.0.0
SQLAlchemy==2.0.23
typing_extensions==4.8.0
Werkzeug==3.0.1

Para dockerizar la Api:
- Instalar y utilizar Docker y Docker Compose para dockerizar la API. Para lo cual deberán:
Configurar un servicio para la aplicación web de Flask (es decir, tendrá su contenedor independiente).
Configurar un servicio para la base de datos MySQL.
Configurar volúmenes para la persistencia de datos, “comunicación” entre contenedores y de estos con el host.
Configurar las variables de <environment> del servicio de MySQL para que sean leídas desde el archivo de variables de entorno (<.env>).
Configurar/crear un archivo de <shell> o <bash> que se encargue de correr aquellos comandos necesarios para el funcionamiento del proyecto (creación de tablas de la base de datos, iniciación del servicio de Gunicorn, ejecución de la aplicación de Flask, etc).
Crear un archivo <sql> para que cree o inicialice el schema de la base de datos.

## Instalación

- Clonar repositorio: Ingresa al repositorio de GitHub del proyecto vas a la carpeta donde deseas clonarlo y en el cmd escribe "git clone https://github.com/ramiroquiro17/EFI_DevOps_Python.git"

- Construir la imagen del Docker: Una vez ingresado el proyecto en una carpeta, podés crear y correr una imagen de Docker a través del cmd con "docker-compose build && docker-compose up"

## Uso

- Podés realizar vistas, creacion, modificaciones o eliminación de información a través de la extensión Postman (podés encontrarlo e instalarlo en la opción de extensiones del Visual Studio Code).

- Una vez en Postman. Podés observar elementos específicos (como posts, usuarios, comentarios, etc) seleccionando la opción GET que te aparece al costado de la barra de navegación y en esta poner "localhost/5000:user" o el nombre de cualquier tabla que deseas visualizar.

- En caso de querer visualizar una fila en específico. Podés especificar el id del elemento con "localhost/5000:user/3"

- Si deseas crear un nuevo elemento, podés seleccionar la opción POST, ingresar "localhost/5000:user/id" e ir a "body" -> opción "raw" -> elegir en text: "JSON" -> Escribir el nuevo elemento que deseas ingresar con las columnas correspondientes (en formato JSON).

- Podés modificar elementos realizando los pasos especificados anteriormente pero eligiendo la opción PUT y especificando el id del elemento que deseas modificar. También podés eliminar algún elemento con la opción DELETE.

## Configuración

- Podés requerir activar las funciones apache y Mysql del XAMPP.

## Solución de prblemas

Si se te genera un error a la hora de subir información o modificar información y no sabes cual es el problema, asegúrese de:

- Tener la opción correcta al lado de la barra de búsqueda dependiendo de la función que deseas reaizar (POST, GET, PUT o DELETE).

- Asegurar que el enlace o puerto estén bien escritos. Ejemplo: localhost/5000:user/3

- Revisar que el tipo de texto sea JSON

- Separar cada columna con una coma

- Asegurar que el nombre de cada columna coincida con los nombres establecidos en el archivo views.

- Tener corriendo el comando flask run --reload






## Docker y docker-compose

####Para los que estaban teniendo problemas con la db.

Con este comando van a borrar los volúmenes asociados al docker-compose del proyecto:

`docker-compose down -v `

Les dejo otro comando, por las dudas que no sea suficiente el anterior, que va a borrar **todas** las imágenes, contenedores y volúmenes que tengan, usenló con cuidado:

`docker system prune -a --volumes`


Una vez hecho eso, les recomiendo borrar los contenedores y reconstruir las imágenes.

Pueden correr:

`docker-compose build && docker-compose up`


Les recomiendo correrlo sin el `-d` al principio así pueden ver los logs más fácil en caso de que algo salga mal.

Luego de eso lo cancelan con `CTRL+C` y lo vuelven a levantar con `docker-compose up -d` o `docker-compose restart`. Luego para frenarlo, usan `docker-compose stop`

Presten **muchísima** atención a las variables de entorno y los valores que ponen. Yo les actualicé el .env.sample para que tengan de referencia. Ojo que les coincida con el `/init/create_schema.sql`, no llegué a configurar las variables de entorno.



## Instalaciones


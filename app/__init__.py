
import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv # Vinculamos el .env para ingresar a la base de datos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(  
    'SQLALCHEMY_DATABASE_URI'
    ) # Indicamos base de datos, usando los datos almacenados en el .env

db = SQLAlchemy(app) # Establecemos instancia con sqlalchemy e iniciamos la base de datos 
migrate = Migrate(app, db) # flask db migrate (generar migración)
ma = Marshmallow(app) # Instancia de marshmallow, recibe como parámetro app.

load_dotenv() # Cargo la variable del entorno (.env)

# Vistas que ejecutará Flask

from app.views import views # Traemos todo lo que está dentro de la carpeta views, donde se importa models. 

# flask db init

# flask db migrate -m 'create_user'

# flask db upgrade
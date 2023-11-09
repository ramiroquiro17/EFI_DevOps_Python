# Este es el archivo principal que ejecuta Flask
import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'PATH_DB'
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

# Cargo la variable de entorno (.env)
load_dotenv()

# Estas son las vistas que Flask ejecutara
from app.views import view
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Validar que las variables críticas existan
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY no está configurada en las variables de entorno")
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL no está configurada en las variables de entorno")

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_almacen.db'

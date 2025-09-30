import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-almacen29-2024'

    # Configuración de PostgreSQL
    DB_USER = os.environ.get('DB_USER') or 'almacen29_user'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'restaurante123'
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_PORT = os.environ.get('DB_PORT') or '5432'
    DB_NAME = os.environ.get('DB_NAME') or 'almacen29_db'

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

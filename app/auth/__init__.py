from flask import Blueprint

# Define el Blueprint. 'auth' es el nombre que usaremos en url_for()
bp = Blueprint('auth', __name__) 

# Importamos las rutas al final para evitar importaciones circulares
from app.auth import routes
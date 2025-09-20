from flask import Flask
from .models import db  # Importaremos la base de datos luego

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # Carga config general

    # Inicializar extensiones (ej: Base de datos)
    db.init_app(app)

    # Registrar blueprints (rutas)
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

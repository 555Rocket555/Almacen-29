from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import click

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # --- REGISTRO DE BLUEPRINTS (VERSIÓN FINAL) ---
    # (Importamos desde los nuevos paquetes)
    from app.auth import bp as auth_bp
    from app.admin import bp as admin_bp
    from app.mesero import bp as mesero_bp

    # (El registro sigue igual, ¡pero ahora apunta a los nuevos paquetes!)
    app.register_blueprint(auth_bp) # (Este es el root '/')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(mesero_bp, url_prefix='/mesero')

    # --- COMANDO CREATE-ADMIN ---
    from app.models import Usuario  # (Esta importación ya es la correcta)

    @app.cli.command("create-admin")
    def create_admin_command():
        """Crea el usuario administrador por defecto."""
        # ... (toda tu lógica de create-admin se queda igual) ...
        admin_existente = Usuario.query.filter_by(email='admin@sistema.com').first()
        if not admin_existente:
            
            print("✅ Usuario administrador creado:")
        else:
            print("✅ Usuario administrador ya existe")
            
    return app
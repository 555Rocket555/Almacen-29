from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Configuración básica para PostgreSQL
    app.config['SECRET_KEY'] = 'clave-secreta-temporal-para-desarrollo'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://almacen_user:password123@localhost/almacen29_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Intentar cargar configuración desde instance/config.py si existe
    instance_config_path = os.path.join(app.root_path, '../instance/config.py')
    if os.path.exists(instance_config_path):
        app.config.from_pyfile(instance_config_path)
        print("✅ Configuración cargada desde instance/config.py")
    else:
        print("⚠️  Usando configuración por defecto - Crea instance/config.py")
    
    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor inicia sesión para acceder a esta página.'
    
    # Registrar blueprints
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)
    
    return app
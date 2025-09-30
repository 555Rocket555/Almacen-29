from app import create_app, db
import os

app = create_app()

@app.cli.command("init-db")
def init_db():
    """Comando para inicializar la base de datos"""
    with app.app_context():
        db.create_all()
        print("✅ Tablas de PostgreSQL creadas correctamente")
        print(f"📊 Base de datos: {app.config['SQLALCHEMY_DATABASE_URI']}")

if __name__ == '__main__':
    with app.app_context():
        # Crear tablas si no existen
        db.create_all()
        print("🚀 Servidor Flask iniciado")
        print(f"📊 Conectado a PostgreSQL: {app.config['SQLALCHEMY_DATABASE_URI']}")

    app.run(debug=True, host='0.0.0.0', port=5000)

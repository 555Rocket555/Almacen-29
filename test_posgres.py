#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa  # ← Importamos SQLAlchemy directamente

app = Flask(__name__)

# Configuración de PostgreSQL - ¡AJUSTA ESTOS VALORES!
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tester:12345@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'test-key'

db = SQLAlchemy(app)

@app.route('/')
def test_db():
    try:
        # Intenta conectar a la base de datos (FORMA CORRECTA)
        with app.app_context():
            with db.engine.connect() as conn:
                result = conn.execute(sa.text('SELECT version()')).fetchone()
        
        return f"✅ ¡Conexión exitosa! PostgreSQL version: {result[0]}"
    
    except Exception as e:
        return f"❌ Error de conexión: {str(e)}"

if __name__ == '__main__':
    print("Probando conexión a PostgreSQL...")
    app.run(debug=True, host='0.0.0.0', port=5001)

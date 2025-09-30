from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.models.usuario import Usuario
from app import db
import psycopg2

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            # Buscar usuario en PostgreSQL
            user = Usuario.query.filter_by(username=username).first()

            if user and user.password == password:  # ¡MEJORAR: usar hash!
                login_user(user)
                flash(f'Bienvenido {username}!', 'success')
                return redirect(url_for('auth.dashboard'))

            flash('Usuario o contraseña incorrectos', 'error')

        return render_template('auth/login.html')

    except psycopg2.OperationalError as e:
        flash('Error de conexión con la base de datos', 'error')
        return render_template('auth/login.html')
    except Exception as e:
        flash('Error interno del servidor', 'error')
        return render_template('auth/login.html')

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return "¡Bienvenido al Dashboard! (Esta es una vista protegida)"

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente', 'info')
    return redirect(url_for('auth.login'))

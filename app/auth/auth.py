from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.services.user_service import UserService
from app.common.auth_helpers import login_required

bp = Blueprint('auth_routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect_to_dashboard(session['user_rol'])

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = UserService.authenticate_user(email, password)

        if user:
            setup_user_session(user)
            flash(f'¡Bienvenido {user.nombre}!', 'success')
            return redirect_to_dashboard(user.rol)
        else:
            flash('Email o contraseña incorrectos', 'danger')

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('auth_routes.login'))  # CORREGIDO: auth_routes.login

# Funciones auxiliares CORREGIDAS
def redirect_to_dashboard(rol):
    if rol == 'admin':
        return redirect(url_for('admin_routes.dashboard'))  # CORREGIDO
    elif rol == 'mesero':
        return redirect(url_for('mesero_routes.dashboard'))  # CORREGIDO
    else:
        return redirect(url_for('auth_routes.login'))  # CORREGIDO

def setup_user_session(user):
    session['user_id'] = user.id
    session['user_nombre'] = user.nombre
    session['user_rol'] = user.rol
    session['user_email'] = user.email

# Ruta temporal para diagnóstico
@bp.route('/test')
def test():
    return "¡Flask está funcionando correctamente!"

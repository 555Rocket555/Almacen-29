from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor inicia sesión para acceder a esta página.', 'warning')
            return redirect(url_for('auth_routes.login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_rol' not in session or session['user_rol'] != 'admin':
            flash('Acceso denegado. Se requieren permisos de administrador.', 'danger')
            return redirect(url_for('auth_routes.login'))
        return f(*args, **kwargs)
    return decorated_function

def mesero_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_rol' not in session or session['user_rol'] != 'mesero':
            flash('Acceso denegado. Se requieren permisos de mesero.', 'danger')  # CORREGIDO: mensaje
            return redirect(url_for('auth_routes.login'))
        return f(*args, **kwargs)
    return decorated_function

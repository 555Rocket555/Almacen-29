from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.usuario import Usuario
from app.helpers.auth_helpers import login_required

bp = Blueprint('auth_routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/login', methods=['GET', 'POST'])
def login():
    # Si ya está logueado, redirigir al dashboard correspondiente
    if 'user_id' in session:
        if session['user_rol'] == 'admin':
            return redirect(url_for('admin_routes.dashboard'))
        return redirect(url_for('auth_routes.login'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        usuario = Usuario.query.filter_by(email=email, activo=True).first()
        print("========Credenciales recibidas========")
        print("Email:", email)
        print("Contraseña:", password)
        print("======================================")        

        if usuario and usuario.check_password(password):
            session['user_id'] = usuario.id
            session['user_nombre'] = usuario.nombre
            session['user_rol'] = usuario.rol
            session['user_email'] = usuario.email

            flash(f'¡Bienvenido {usuario.nombre}!', 'success')

            if usuario.rol == 'admin':
                return redirect(url_for('admin_routes.dashboard'))
            else:
                flash('Tu rol no tiene acceso al sistema en este momento.', 'info')
                return redirect(url_for('auth_routes.login'))

        flash('Email o contraseña incorrectos', 'danger')

        print("========Credenciales recibidas========")
        print("Email:", email)
        print("Contraseña:", password)
        print("======================================")        

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('auth_routes.login'))

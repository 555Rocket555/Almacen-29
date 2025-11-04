from flask import render_template, request, redirect, url_for, session, flash
from app import db
from app.models import Usuario
from app.auth import bp
from app.common.auth_helpers import login_required


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect_to_dashboard(session['user_rol'])

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Usuario.query.filter_by(email=email).first()

        if user and user.check_password(password):
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

    return redirect(url_for('auth.login')) 


def redirect_to_dashboard(rol):
    if rol == 'admin':
        return redirect(url_for('admin.dashboard'))
    elif rol == 'mesero':
        return redirect(url_for('mesero.dashboard'))
    else:
        return redirect(url_for('auth.login'))

def setup_user_session(user):
    session['user_id'] = user.id
    session['user_nombre'] = user.nombre
    session['user_rol'] = user.rol
    session['user_email'] = user.email

@bp.route('/test')
def test():
    return "¡Blueprint de Auth funcionando!"

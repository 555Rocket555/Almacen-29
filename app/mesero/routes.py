from flask import render_template, session
from app.mesero import bp


from app.common.auth_helpers import login_required, mesero_required


@bp.route('/dashboard')
@login_required
@mesero_required
def dashboard():
    nombre_usuario = session.get('user_nombre', 'Mesero')
    return render_template('mesero/dashboard.html', nombre=nombre_usuario)

from flask import Blueprint, render_template, session
from app.helpers.auth_helpers import login_required, mesero_required

bp = Blueprint('mesero_routes', __name__)  # Nombre cambiado

@bp.route('/dashboard')
@login_required
@mesero_required
def dashboard():
    nombre_usuario = session.get('user_nombre', 'Mesero')
    return render_template('mesero/dashboard.html', nombre=nombre_usuario)

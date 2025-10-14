from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.helpers.auth_helpers import login_required, admin_required

bp = Blueprint('admin_routes', __name__)  # Nombre cambiado

@bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    stats = UserService.get_user_stats()
    return render_template('admin/dashboard.html', **stats)

@bp.route('/usuarios')
@login_required
@admin_required
def lista_usuarios():
    usuarios = UserRepository.get_all()
    return render_template('admin/lista_usuarios.html', usuarios=usuarios)

@bp.route('/registrar-usuario', methods=['GET', 'POST'])
@login_required
@admin_required
def registrar_usuario():
    if request.method == 'POST':
        try:
            user = UserService.register_user(request.form)
            flash(f'Usuario {user.nombre} registrado exitosamente como {user.rol}', 'success')
            return redirect(url_for('admin_routes.lista_usuarios'))  # CORREGIDO
        except ValueError as e:
            flash(str(e), 'danger')

    return render_template('admin/registrar_usuario.html')

from flask import render_template, redirect, url_for, flash, request
from app import db  # <--- Importamos la DB
from app.models import Usuario  # <--- Importamos el modelo
from app.admin import bp  # <--- Importamos el Blueprint local

# (Asumiendo que 'helpers' se movió a 'common')
from app.common.auth_helpers import login_required, admin_required

# (Ya no necesitamos UserService ni UserRepository)


@bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    # --- LÓGICA CONSOLIDADA ---
    # (Esta es la lógica que probablemente estaba en UserService.get_user_stats())
    stats = {
        'total_usuarios': Usuario.query.count(),
        'admin_count': Usuario.query.filter_by(rol='admin').count(),
        'mesero_count': Usuario.query.filter_by(rol='mesero').count(),
        'activos_count': Usuario.query.filter_by(activo=True).count()
    }
    # --- FIN LÓGICA ---
    return render_template('admin/dashboard.html', **stats)


@bp.route('/usuarios')
@login_required
@admin_required
def lista_usuarios():
    # --- LÓGICA CONSOLIDADA ---
    # (Lógica de UserRepository.get_all())
    usuarios = Usuario.query.all()
    # --- FIN LÓGICA ---
    return render_template('admin/lista_usuarios.html', usuarios=usuarios)


@bp.route('/registrar-usuario', methods=['GET', 'POST'])
@login_required
@admin_required
def registrar_usuario():
    if request.method == 'POST':
        try:
            # --- LÓGICA CONSOLIDADA ---
            # (Lógica de UserService.register_user())

            # 1. Obtenemos datos
            email = request.form.get('email')
            nombre = request.form.get('nombre')
            password = request.form.get('password')
            rol = request.form.get('rol')

            # 2. Validamos (Lógica del Servicio)
            if not email or not nombre or not password or not rol:
                raise ValueError("Todos los campos son requeridos.")

            if Usuario.query.filter_by(email=email).first():
                raise ValueError(f"El email '{email}' ya está registrado.")

            # 3. Creamos (Lógica del Repositorio)
            user = Usuario(
                nombre=nombre,
                email=email,
                rol=rol
            )
            user.set_password(password) # Usamos el método del modelo

            db.session.add(user)
            db.session.commit()
            # --- FIN LÓGICA ---

            flash(f'Usuario {user.nombre} registrado exitosamente como {user.rol}', 'success')
            # Usamos el nuevo nombre del Blueprint: 'admin'
            return redirect(url_for('admin.lista_usuarios')) 

        except ValueError as e:
            db.session.rollback() # Buena práctica
            flash(str(e), 'danger')
        except Exception as e:
            db.session.rollback()
            flash(f'Error inesperado: {e}', 'danger')

    return render_template('admin/registrar_usuario.html')
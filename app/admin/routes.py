from flask import render_template, redirect, url_for, flash, request, jsonify
from app import db
from app.models import Usuario
from app.admin import bp
from app.common.auth_helpers import login_required, admin_required


@bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    stats = {
        'total_usuarios': Usuario.query.count(),
        'admin_count': Usuario.query.filter_by(rol='admin').count(),
        'mesero_count': Usuario.query.filter_by(rol='mesero').count(),
        'activos_count': Usuario.query.filter_by(activo=True).count()
    }
    return render_template('admin/dashboard.html', **stats)


@bp.route('/usuarios')
@login_required
@admin_required
def lista_usuarios():
    usuarios = Usuario.query.all()
    return render_template('admin/lista_usuarios.html', usuarios=usuarios)


# --- "C" (Create) ---
# GET: Muestra el formulario de registro
@bp.route('/registrar-usuario', methods=['GET'])
@login_required
@admin_required
def registrar_usuario_form():
    # Renderiza la plantilla en modo "Crear"
    return render_template('admin/registrar_usuario.html', 
                           titulo='Registrar Nuevo Usuario',
                           icono='fa-user-plus')

# POST: Procesa el formulario de registro
@bp.route('/registrar-usuario', methods=['POST'])
@login_required
@admin_required
def registrar_usuario_post():
    try:
        email = request.form.get('email')
        nombre = request.form.get('nombre')
        password = request.form.get('password')
        confirmar_password = request.form.get('confirmar_password')
        rol = request.form.get('rol')
        

        # --- Validaciones ---
        if not email or not nombre or not password or not rol:
            raise ValueError("Nombre, email, contraseña y rol son requeridos.")
        if password != confirmar_password:
            raise ValueError("Las contraseñas no coinciden.")
        if Usuario.query.filter_by(email=email).first():
            raise ValueError(f"El email '{email}' ya está registrado.")
        
        # --- Creación de Usuario ---
        user = Usuario(
            nombre=nombre,
            email=email,
            rol=rol,
            activo=True# <--- Guardamos el estado 'activo'
        )
        user.set_password(password) # Usamos tu método del modelo

        db.session.add(user)
        db.session.commit()
        
        flash(f'Usuario {user.nombre} registrado exitosamente.', 'success')
        return redirect(url_for('admin.lista_usuarios'))

    except ValueError as e:
        flash(str(e), 'danger')
        # Regresamos al formulario con los datos (para no perderlos)
        return render_template('admin/registrar_usuario.html', 
                               titulo='Registrar Nuevo Usuario',
                               icono='fa-user-plus',
                               form_data=request.form), 400
    except Exception as e:
        db.session.rollback()
        flash(f'Error inesperado: {e}', 'danger')
        return redirect(url_for('admin.registrar_usuario_form')) # Redirige a la ruta GET


# --- "U" (Update) ---
# GET: Muestra el formulario de edición
@bp.route('/usuarios/editar/<int:id>', methods=['GET'])
@login_required
@admin_required
def editar_usuario_form(id):
    usuario = Usuario.query.get_or_404(id)
    # Renderiza la MISMA plantilla, pero en modo "Editar"
    return render_template('admin/registrar_usuario.html', 
                           titulo=f'Editar Usuario: {usuario.nombre}',
                           icono='fa-user-edit',
                           usuario=usuario) # <--- La clave está aquí

# POST: Procesa el formulario de edición
@bp.route('/usuarios/editar/<int:id>', methods=['POST'])
@login_required
@admin_required
def editar_usuario_post(id):
    usuario = Usuario.query.get_or_404(id)
    try:
        # Obtenemos datos
        usuario.nombre = request.form.get('nombre')
        usuario.email = request.form.get('email')
        usuario.rol = request.form.get('rol')
        usuario.activo = 'activo' in request.form # <--- Lógica para el checkbox 'activo'
        password = request.form.get('password')
        confirmar_password = request.form.get('confirmar_password')

        # --- Validaciones ---
        if not usuario.nombre or not usuario.email or not usuario.rol:
            raise ValueError("Nombre, email y rol son requeridos.")
        
        # Validar email duplicado (excepto él mismo)
        email_existente = Usuario.query.filter_by(email=usuario.email).first()
        if email_existente and email_existente.id != usuario.id:
            raise ValueError(f"El email '{usuario.email}' ya está en uso por otro usuario.")

        # --- Lógica de Contraseña Opcional ---
        if password: # Si el campo de contraseña no está vacío...
            if password != confirmar_password:
                raise ValueError("Las contraseñas no coinciden.")
            usuario.set_password(password) # ...la actualizamos
        
        # --- Guardar Cambios ---
        db.session.commit() # Solo commit, porque el usuario ya existía
        
        flash(f'Usuario {usuario.nombre} actualizado exitosamente.', 'success')
        return redirect(url_for('admin.lista_usuarios'))

    except ValueError as e:
        flash(str(e), 'danger')
        # Regresamos al formulario de edición
        return render_template('admin/registrar_usuario.html', 
                               titulo=f'Editar Usuario: {usuario.nombre}',
                               icono='fa-user-edit',
                               usuario=usuario), 400
    except Exception as e:
        db.session.rollback()
        flash(f'Error inesperado: {e}', 'danger')
        return redirect(url_for('admin.editar_usuario_form', id=id))


# --- "D" (Delete) ---
@bp.route('/usuarios/eliminar/<int:id>', methods=['POST'])
@login_required
@admin_required
def eliminar_usuario(id):
    try:
        usuario = Usuario.query.get_or_404(id)
        
        # (Validación de seguridad - ¡IMPORTANTE!)
        if usuario.email == 'admin@sistema.com': # <-- Cambia esto si tu admin principal tiene otro email
             flash('No se puede eliminar al administrador principal.', 'danger')
             return redirect(url_for('admin.lista_usuarios'))

        nombre_usuario = usuario.nombre
        db.session.delete(usuario)
        db.session.commit()
        flash(f'Usuario {nombre_usuario} eliminado permanentemente.', 'success')
    
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar usuario: {e}', 'danger')

    return redirect(url_for('admin.lista_usuarios'))

# --- RUTA PARA EL SWITCH DE 'ACTIVO' ---
@bp.route('/usuarios/toggle-activo/<int:id>', methods=['POST'])
@login_required
@admin_required
def toggle_activo(id):
    try:
        usuario = Usuario.query.get_or_404(id)
        
        # Validación de seguridad
        if usuario.email == 'admin@sistema.com': # O tu email de admin
             return jsonify({'success': False, 'message': 'No se puede desactivar al admin principal.'}), 403

        # Invertimos el estado
        usuario.activo = not usuario.activo
        db.session.commit()
        
        nuevo_estado_texto = "Activo" if usuario.activo else "Inactivo"
        return jsonify({
            'success': True, 
            'message': f'Usuario {usuario.nombre} ahora está {nuevo_estado_texto}.',
            'nuevo_estado': usuario.activo  # Enviamos el booleano
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500
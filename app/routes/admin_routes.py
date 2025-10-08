from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models.usuario import Usuario
from app.helpers.auth_helpers import login_required, admin_required

bp = Blueprint('admin_routes', __name__)

@bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    total_usuarios = Usuario.query.count()
    return render_template('admin/dashboard.html', total_usuarios=total_usuarios)

@bp.route('/usuarios')
@login_required
@admin_required
def lista_usuarios():
    usuarios = Usuario.query.order_by(Usuario.fecha_creacion.desc()).all()
    return render_template('admin/lista_usuarios.html', usuarios=usuarios)

@bp.route('/registrar-usuario', methods=['GET', 'POST'])
@login_required
@admin_required
def registrar_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmar_password = request.form.get('confirmar_password')
        rol = request.form.get('rol')
        print("datos:nombre", nombre)
        print("datos:email" , email)
    
        # Validaciones básicas
        if not all([nombre, email, password, confirmar_password, rol]):
            flash('Todos los campos son obligatorios', 'danger')
            return redirect(url_for('admin_routes.registrar_usuario'))

        if password != confirmar_password:
            flash('Las contraseñas no coinciden', 'danger')
            return redirect(url_for('admin_routes.registrar_usuario'))

        if len(password) < 6:
            flash('La contraseña debe tener al menos 6 caracteres', 'danger')
            return redirect(url_for('admin_routes.registrar_usuario'))

        # Verificar si el email ya existe
        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            flash('Este email ya está registrado', 'danger')
            return redirect(url_for('admin_routes.registrar_usuario'))

        # Crear nuevo usuario
        nuevo_usuario = Usuario(
            nombre=nombre,
            email=email,
            rol=rol
        )
        nuevo_usuario.set_password(password)

        db.session.add(nuevo_usuario)
        db.session.commit()

        flash(f'Usuario {nuevo_usuario.nombre} registrado exitosamente como {nuevo_usuario.rol}', 'success')
        return redirect(url_for('admin_routes.lista_usuarios'))

    return render_template('admin/registrar_usuario.html')

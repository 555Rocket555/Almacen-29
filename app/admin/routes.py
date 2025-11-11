from flask import render_template, redirect, url_for, flash, request, jsonify
from app import db
from app.models import Usuario
from app.models.productos import Producto
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


@bp.route('/registrar-usuario', methods=['GET'])
@login_required
@admin_required
def registrar_usuario_form():

    return render_template('admin/registrar_usuario.html', 
                           titulo='Registrar Nuevo Usuario',
                           icono='fa-user-plus')

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
        

        if not email or not nombre or not password or not rol:
            raise ValueError("Nombre, email, contraseña y rol son requeridos.")
        if password != confirmar_password:
            raise ValueError("Las contraseñas no coinciden.")
        if Usuario.query.filter_by(email=email).first():
            raise ValueError(f"El email '{email}' ya está registrado.")
        
        user = Usuario(
            nombre=nombre,
            email=email,
            rol=rol,
            activo=True
        )
        user.set_password(password) 

        db.session.add(user)
        db.session.commit()
        
        flash(f'Usuario {user.nombre} registrado exitosamente.', 'success')
        return redirect(url_for('admin.lista_usuarios'))

    except ValueError as e:
        flash(str(e), 'danger')
        
        return render_template('admin/registrar_usuario.html', 
                               titulo='Registrar Nuevo Usuario',
                               icono='fa-user-plus',
                               form_data=request.form), 400
    except Exception as e:
        db.session.rollback()
        flash(f'Error inesperado: {e}', 'danger')
        return redirect(url_for('admin.registrar_usuario_form')) 

@bp.route('/usuarios/editar/<int:id>', methods=['GET'])
@login_required
@admin_required
def editar_usuario_form(id):
    usuario = Usuario.query.get_or_404(id)

    return render_template('admin/registrar_usuario.html', 
                           titulo=f'Editar Usuario: {usuario.nombre}',
                           icono='fa-user-edit',
                           usuario=usuario) 


@bp.route('/usuarios/editar/<int:id>', methods=['POST'])
@login_required
@admin_required
def editar_usuario_post(id):
    usuario = Usuario.query.get_or_404(id)
    try:
        
        usuario.nombre = request.form.get('nombre')
        usuario.email = request.form.get('email')
        usuario.rol = request.form.get('rol')
        usuario.activo = 'activo' in request.form 
        password = request.form.get('password')
        confirmar_password = request.form.get('confirmar_password')

        
        if not usuario.nombre or not usuario.email or not usuario.rol:
            raise ValueError("Nombre, email y rol son requeridos.")
        
        
        email_existente = Usuario.query.filter_by(email=usuario.email).first()
        if email_existente and email_existente.id != usuario.id:
            raise ValueError(f"El email '{usuario.email}' ya está en uso por otro usuario.")

        
        if password: 
            if password != confirmar_password:
                raise ValueError("Las contraseñas no coinciden.")
            usuario.set_password(password) 
        
        
        db.session.commit() 
        
        flash(f'Usuario {usuario.nombre} actualizado exitosamente.', 'success')
        return redirect(url_for('admin.lista_usuarios'))

    except ValueError as e:
        flash(str(e), 'danger')
    
        return render_template('admin/registrar_usuario.html', 
                               titulo=f'Editar Usuario: {usuario.nombre}',
                               icono='fa-user-edit',
                               usuario=usuario), 400
    except Exception as e:
        db.session.rollback()
        flash(f'Error inesperado: {e}', 'danger')
        return redirect(url_for('admin.editar_usuario_form', id=id))



@bp.route('/usuarios/eliminar/<int:id>', methods=['POST'])
@login_required
@admin_required
def eliminar_usuario(id):
    try:
        usuario = Usuario.query.get_or_404(id)
        

        if usuario.email == 'admin@sistema.com': 
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


@bp.route('/usuarios/toggle-activo/<int:id>', methods=['POST'])
@login_required
@admin_required
def toggle_activo(id):
    try:
        usuario = Usuario.query.get_or_404(id)
        
        if usuario.email == 'admin@sistema.com': 
             return jsonify({'success': False, 'message': 'No se puede desactivar al admin principal.'}), 403

        usuario.activo = not usuario.activo
        db.session.commit()
        
        nuevo_estado_texto = "Activo" if usuario.activo else "Inactivo"
        return jsonify({
            'success': True, 
            'message': f'Usuario {usuario.nombre} ahora está {nuevo_estado_texto}.',
            'nuevo_estado': usuario.activo  
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500
    return render_template('admin/registrar_usuario.html')


@bp.route('/productos')
@login_required
@admin_required
def lista_productos():
    try:
        todos_los_productos = Producto.query.all()
    except Exception as e:
        flash(f'Error al cargar productos: {e}', 'danger')
        todos_los_productos = []

    return render_template(
        'admin/lista_productos.html', 
        productos=todos_los_productos
        )

@bp.route('/productos/registrar', methods=['GET', 'POST'])
@login_required
@admin_required
def registrar_producto():
    
    if request.method == 'POST':
        try:
            
            nombre = request.form.get('nombre')
            descripcion = request.form.get('descripcion')
            
            try:
                precio = float(request.form.get('precio', 0))
                costo = float(request.form.get('costo', 0))
            except (ValueError, TypeError):
                precio = 0.0
                costo = 0.0
            
            
            if not nombre or precio <= 0:
                raise ValueError("El 'Nombre' y un 'Precio' válido son requeridos.")

            nuevo_producto = Producto(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                costo=costo, 
                disponible=True 
            )

            
            db.session.add(nuevo_producto)
            db.session.commit()
            
            flash(f'Producto "{nombre}" registrado exitosamente.', 'success')
            return redirect(url_for('admin.lista_productos'))

        except ValueError as e:
            flash(str(e), 'danger')
            
            return render_template('admin/registrar_producto.html', 
                                   titulo='Registrar Producto',
                                   form_data=request.form), 400
        except Exception as e:
            db.session.rollback()
            flash(f'Error inesperado al crear el producto: {e}', 'danger')
            
    
    return render_template(
        'admin/registrar_producto.html',
        titulo='Registrar Nuevo Producto'
    )


@bp.route('/productos/toggle-disponible/<int:id>', methods=['POST'])
@login_required
@admin_required
def toggle_disponible(id):
    try:
        producto = Producto.query.get_or_404(id)
        
        producto.disponible = not producto.disponible
        db.session.commit()
        
        nuevo_estado_texto = "Disponible" if producto.disponible else "Agotado"
        return jsonify({
            'success': True, 
            'message': f'Producto {producto.nombre} ahora está {nuevo_estado_texto}.',
            'nuevo_estado_texto': nuevo_estado_texto,
            'nuevo_estado_bool': producto.disponible
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500


@bp.route('/productos/editar/<int:id>', methods=['GET'])
@login_required
@admin_required
def editar_producto_form(id):
    
    producto = Producto.query.get_or_404(id)

    return render_template(
        'admin/registrar_producto.html', 
        titulo=f'Editar Producto: {producto.nombre}',
        producto=producto  
    )


@bp.route('/productos/editar/<int:id>', methods=['POST'])
@login_required
@admin_required
def editar_producto_post(id):
    
    producto = Producto.query.get_or_404(id)
    
    try:

        producto.nombre = request.form.get('nombre')
        producto.descripcion = request.form.get('descripcion')
        
        try:
            producto.precio = float(request.form.get('precio', 0))
            producto.costo = float(request.form.get('costo', 0))
        except (ValueError, TypeError):
            producto.precio = 0.0
            producto.costo = 0.0


        if not producto.nombre or producto.precio <= 0:
            raise ValueError("El 'Nombre' y un 'Precio' válido son requeridos.")
        

        db.session.commit()
        
        flash(f'Producto "{producto.nombre}" actualizado exitosamente.', 'success')
        return redirect(url_for('admin.lista_productos'))

    except ValueError as e:
        flash(str(e), 'danger')

        return render_template('admin/registrar_producto.html', 
                               titulo=f'Editar Producto: {producto.nombre}',
                               producto=producto), 400
    except Exception as e:
        db.session.rollback()
        flash(f'Error inesperado al actualizar: {e}', 'danger')
        return redirect(url_for('admin.editar_producto_form', id=id))



@bp.route('/productos/eliminar/<int:id>', methods=['POST'])
@login_required
@admin_required
def eliminar_producto(id):
    try:
        producto = Producto.query.get_or_404(id)
        nombre_producto = producto.nombre
        
        # (Aquí podríamos añadir una protección futura para
        #  no borrar productos que ya están en órdenes pagadas)
        
        db.session.delete(producto)
        db.session.commit()
        
        flash(f'Producto "{nombre_producto}" eliminado permanentemente.', 'success')
    
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar el producto: {e}', 'danger')

    return redirect(url_for('admin.lista_productos'))
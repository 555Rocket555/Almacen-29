 #En auth routes

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

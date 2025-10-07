from app import create_app, db
from app.models.usuario import Usuario

app = create_app()

with app.app_context():
    # Crear todas las tablas
    db.create_all()

    # Verificar si ya existe un admin
    admin_existente = Usuario.query.filter_by(email='admin@sistema.com').first()

    if not admin_existente:
        # Crear usuario admin por defecto
        admin = Usuario(
            nombre='Administrador Principal',
            email='admin@sistema.com',
            rol='admin'
        )
        admin.set_password('admin123')

        db.session.add(admin)
        db.session.commit()
        print("✅ Usuario administrador creado:")
        print("   Email: admin@sistema.com")
        print("   Password: admin123")
    else:
        print("✅ Usuario administrador ya existe")

    print("✅ Tablas creadas en la base de datos 'almacen'")

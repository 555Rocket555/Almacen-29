from app.repositories.user_repository import UserRepository
from flask import flash

class UserService:

    @staticmethod
    def authenticate_user(email, password):
        user = UserRepository.find_by_email(email)
        if user and user.check_password(password):
            return user
        return None

    @staticmethod
    def register_user(user_data):
        nombre = user_data.get('nombre')
        email = user_data.get('email')
        password = user_data.get('password')
        confirm_password = user_data.get('confirmar_password')
        rol = user_data.get('rol')

        # Validaciones
        if not all([nombre, email, password, confirm_password, rol]):
            raise ValueError('Todos los campos son obligatorios')

        if password != confirm_password:
            raise ValueError('Las contraseñas no coinciden')

        if len(password) < 6:
            raise ValueError('La contraseña debe tener al menos 6 caracteres')

        if UserRepository.find_by_email(email):
            raise ValueError('Este email ya está registrado')

        return UserRepository.create(nombre, email, rol, password)

    @staticmethod
    def get_user_stats():
        return {
            'total_usuarios': UserRepository.count_all()
        }

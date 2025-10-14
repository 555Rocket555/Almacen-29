from app.models.usuario import Usuario
from app import db

class UserRepository:
    
    @staticmethod
    def find_by_id(user_id):
        return Usuario.query.get(user_id)
    
    @staticmethod
    def find_by_email(email):
        return Usuario.query.filter_by(email=email, activo=True).first()
    
    @staticmethod
    def get_all():
        return Usuario.query.order_by(Usuario.fecha_creacion.desc()).all()
    
    @staticmethod
    def count_all():
        return Usuario.query.count()
    
    @staticmethod
    def save(user):
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def create(nombre, email, rol, password):
        user = Usuario(nombre=nombre, email=email, rol=rol)
        user.set_password(password)
        return UserRepository.save(user)
    
    @staticmethod
    def delete(user):
        user.activo = False
        db.session.commit()
        return user

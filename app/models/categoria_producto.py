from app import db
from .productos import Producto

class CategoriaProducto(db.Model):
    __tablename__ = 'categorias_producto'
    
    id = db.Column(db.Integer, primary_key=True) 
    nombre = db.Column(db.String(100), nullable=False, unique=True) 

    productos = db.relationship('Producto', back_populates='categoria') 
    
    def __repr__(self):
        return f'<Categoria {self.nombre}>'
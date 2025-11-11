from app import db

class ProductoIngrediente(db.Model):
    __tablename__ = 'producto_ingredientes'
    id = db.Column(db.Integer, primary_key=True) 
    cantidad_requerida = db.Column(db.Float, nullable=False) 
    
    # Llaves Foráneas
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False) 
    insumo_id = db.Column(db.Integer, db.ForeignKey('insumos.id'), nullable=False)
    # Relaciones (Muchos-a-Uno)
    producto = db.relationship('Producto', back_populates='ingredientes') 
    insumo = db.relationship('Insumo', back_populates='productos_asociados')
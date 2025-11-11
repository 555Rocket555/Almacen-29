from app import db

class Insumo(db.Model):
    __tablename__ = 'insumos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    cantidad_disponible = db.Column(db.Float, nullable=False, default=0)
    unidad_medida = db.Column(db.String(20)) # Ej: 'kg', 'litro', 'unidad'
    stock_minimo = db.Column(db.Float, default=0)
    costo_unitario = db.Column(db.Float, default=0)
    
    productos_asociados = db.relationship('ProductoIngrediente', back_populates='insumo')

    def __repr__(self):
        return f'<Insumo {self.nombre}>'

    def esta_bajo_stock(self):
        return self.cantidad_disponible <= self.stock_minimo
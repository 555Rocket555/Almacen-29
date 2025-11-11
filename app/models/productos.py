from app import db

class Producto(db.Model):
    __tablename__ = 'productos' 
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True) 
    precio = db.Column(db.Float, nullable=False, default=0) 

    costo = db.Column(db.Float, default=0) 
    
    disponible = db.Column(db.Boolean, default=True) 
    
    tiempo_preparacion = db.Column(db.Integer) 

    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias_producto.id'), nullable=True)

    categoria = db.relationship('CategoriaProducto', back_populates='productos')

    detalles_orden = db.relationship('OrdenDetalle', back_populates='producto') 

    ingredientes = db.relationship('ProductoIngrediente', back_populates='producto') 


    def __repr__(self):
        return f'<Producto {self.id}: {self.nombre}>'

    
    def esta_disponible(self):
        return self.disponible
from app import db

class OrdenDetalle(db.Model):
    __tablename__ = 'orden_detalles'
    
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float)
    
    orden_id = db.Column(db.Integer, db.ForeignKey('ordenes.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    
    producto = db.relationship('Producto', back_populates='detalles_orden')
    orden = db.relationship('Orden', back_populates='detalles')

    def __repr__(self):
        return f'<OrdenDetalle {self.id}>'
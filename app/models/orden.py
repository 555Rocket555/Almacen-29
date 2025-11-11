from app import db
from datetime import datetime

class Orden(db.Model):
    __tablename__ = 'ordenes'
    
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(50), default='pendiente') 
    tipo_orden = db.Column(db.String(50)) 
    total = db.Column(db.Float, default=0.0)
    notas = db.Column(db.Text)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    

    detalles = db.relationship('OrdenDetalle', back_populates='orden')

    def __repr__(self):
        return f'<Orden {self.id}>'
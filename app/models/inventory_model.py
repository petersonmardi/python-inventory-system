from ..extensions import db 
from datetime import datetime as dt

class InventoryModel(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float(16), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=dt.now)


    def __repr__(self):
        return f'Name: {self.name}'
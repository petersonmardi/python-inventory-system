from ..extensions import db 
from datetime import datetime as dt
from ..extensions import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=dt.now)

    def __repr__(self):
        return f'Name: {self.first_name}'
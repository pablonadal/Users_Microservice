from dataclasses import dataclass
from app import db


@dataclass
class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique = True ,nullable=False)
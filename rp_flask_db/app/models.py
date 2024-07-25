from . import db

class Gold(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer, nullable=True)

class Pickaxe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    strength = db.Column(db.Integer, nullable=False)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})


db = SQLAlchemy(metadata=metadata)

class User(db.Model):
  __tablename__ = 'users' 

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String)

class Gold(db.Model):
  __tablename__ = 'gold'

  id = db.Column(db.Integer, primary_key=True)
  amount = db.Column(db.Integer)
  usernameid = db.Column(db.Integer, db.ForeignKey('users.id')) 

class Pickaxe(db.Model):
  __tablename__ = 'pickaxe'

  id = db.Column(db.Integer, primary_key=True) 
  strength = db.Column(db.Integer, nullable=False)
  usernameid = db.Column(db.Integer, db.ForeignKey('users.id')) 
  
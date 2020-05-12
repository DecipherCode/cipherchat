from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class users(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    passhash = db.Column(db.String, nullable=False)


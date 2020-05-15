import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


class userdata(db.Model):
    __tablename__="userdata"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    passhash = db.Column(db.String, nullable=False)
    datetime = db.Column(db.DateTime(timezone=True), default=func.now())
    avatar_id = db.Column(db.Integer, nullable=False)


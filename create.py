import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ltoxbcumoikvjg:5e0189eb9f387a3af26aec138c0c6ddae9b53c5885075693b0c4f11095e7938e@ec2-35-169-254-43.compute-1.amazonaws.com:5432/dcni7jifo8v66s"


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()

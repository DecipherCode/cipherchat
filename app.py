import os

from models import *

from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = ""
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#db.init_app(app)
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    try:
        username=request.form.get("username")
        password=request.form.get("password")
    except:
        return render_template("error.html",message="error with username and password input")
    

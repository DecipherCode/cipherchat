import os

from models import *

from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ltoxbcumoikvjg:5e0189eb9f387a3af26aec138c0c6ddae9b53c5885075693b0c4f11095e7938e@ec2-35-169-254-43.compute-1.amazonaws.com:5432/dcni7jifo8v66s"
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
socketio = SocketIO(app)

def main():
    db.createall()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home" ,methods=["POST"])
def home():
    username=request.form.get("username")
    password=request.form.get("password")
    user = users.query.filter_by(username=username).first()
    if user is None:
        return render_template('construction.html',message="Invalid username or password")
    else:
        if check_password_hash(user.passhash,password):
            return render_template('construction.html',message="login successful!")
        else:
            return "Wrong Password"

@app.route("/register",methods=["POST"])
def register():
    username=request.form.get("username")
    password=request.form.get("password")
    check=users.query.filter_by(username=username).first()
    if check is None:
        passhash=generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        add=users(username=username,passhash=passhash)
        db.session.add(add)
        db.session.commit()
        return render_template('construction.html',message="Account successfully created please go back and try to login :)")
    else:
        return render_template('construction.html',message="Something went wrong")



if __name__ == "__main__":
# Allows for command line interaction with Flask application
    with app.app_context():
        main()
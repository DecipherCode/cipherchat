import os
import datetime
from models import *

from flask import Flask,render_template,request,jsonify
from flask_socketio import SocketIO, emit
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rvlmycroyzfgkn:0eeb3d0d92220e66bbb4eb2c63f42a1ebdcd0c7bcba1c2a2f7fc268b5df20463@ec2-34-202-88-122.compute-1.amazonaws.com:5432/d6htgff90r5lfq"
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
socketio = SocketIO(app)

def main():
    db.createall()

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        name = request.form.get("Name")
        username=request.form.get("username")
        gender=request.form.get("gender")
        password=request.form.get("password")
        passhash=generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        DT = datetime.datetime.now()
        if gender=='M':
            avatar_id = 0
        elif gender=='F':
            avatar_id = 4
        else:
            avatar_id = 8
        print(datetime)
        user = userdata(name=name,username=username,gender=gender,passhash=passhash,datetime=DT,avatar_id = avatar_id)
        db.session.add(user)
        db.session.commit()
        return render_template('Registration_Success.html')

@app.route("/home" ,methods=["POST"])
def home():
    username=request.form.get("username")
    password=request.form.get("password")
    user = users.query.filter_by(username=username).first()
    if user is None:
        return render_template('construction.html',message="Invalid username or password")
    else:
        if check_password_hash(user.passhash,password):
            return render_template("home.html")
        else:
            return "Wrong Password"

@app.route("/API/usernames",methods = ["POST","GET"])
def usernames():
    usernames = db.session.query(userdata.username).all()
    u_list = [usernames[i][0] for i in range(len(usernames))]
    return jsonify({"users":u_list})

if __name__ == "__main__":
# Allows for command line interaction with Flask application
    with app.app_context():
        main()
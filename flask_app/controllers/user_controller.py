from flask_app import app
from flask import  render_template, request, redirect, session
from flask_app.models.user import User

@app.route("/")
def index():
    x = User.get_all()
    print(x)
    return render_template("index.html", all_users = x)

@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/create_user", methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save_user(data)
    return redirect ("/")

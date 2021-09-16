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

@app.route("/user/<int:id>")
def one_user(id):
    data = {
        "user_id" : id
    }
    a_user = User.one_user(data)
    print(one_user)
    return render_template("one_user.html", one_user = a_user)

@app.route("/edit_user/<int:id>")
def edit_user(id):
    
    data = {
        "user_id" : id
    }
    edit_user = User.one_user(data)
    return render_template("update_user.html", one_user = edit_user)

@app.route("/update_user/<int:id>", methods=['POST'])
def update_user(id):
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "id" : id
    }
    User.update_user(data)
    return redirect ("/")

@app.route("/delete_user/<int:id>")
def delete_user(id):
    data = {
        "id" : id
    }
    User.delete_user(data)
    return redirect ("/")
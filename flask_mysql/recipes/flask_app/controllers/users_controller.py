from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask import flash
import re

bcrypt = Bcrypt(app)


# Front landing page
@app.route("/")
def landing():
    return render_template("index.html")


# Route for creating a new user with validations
@app.route("/users/create", methods=["POST"])
def create_user():
    print(request.form)
    if not User.validator(request.form):
        return redirect("/")
    hash_pass = bcrypt.generate_password_hash(request.form["password"])
    data = {
        **request.form,
        'password': hash_pass
    }
    new_id = User.create(data)
    print(new_id)
    session["user_id"] = new_id
    session["first_name"] = request.form["first_name"]
    return redirect("/recipes")


# Route for processing user login with password/email confirmation
@app.route("/users/login_process", methods=["POST"])
def login():
    data = {
        "email": request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("User information is invalid")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("*User information is invalid*")
        return redirect("/")
    session["user_id"] = user_in_db.id
    session["first_name"] = user_in_db.first_name
    return redirect("/recipes")


# Route for logout and clear session
@app.route("/users/logout")
def logout():
    session.clear()
    return redirect("/")

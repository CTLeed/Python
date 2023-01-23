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


# Route to render registration template
@app.route("/users/register")
def register():
    return render_template("reg.html")


# Route to render login template
@app.route("/users/login")
def user_login():
    return render_template("login.html")


# Route to render individual user's main page
@app.route("/dashboard/<int:id>")
def main_page(id):
    if not "user_id" in session:
        return redirect("/")
    user = User.get_one({"id": id})
    print(user.expenses)
    return render_template("user_main.html", user=user)


# Route for creating a new user with validations
@app.route("/users/create", methods=["POST"])
def create_user():
    print(request.form)
    if not User.validator(request.form):
        return redirect("/users/register")
    hash_pass = bcrypt.generate_password_hash(request.form["password"])
    data = {
        **request.form,
        'password': hash_pass
    }
    new_id = User.create(data)
    print(new_id)
    session["user_id"] = new_id
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    return redirect(f"/dashboard/{new_id}")


# Route for processing user login with password/email confirmation
@app.route("/users/login_process", methods=["POST"])
def login():
    data = {
        "email": request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("User information is invalid", "log")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("*User information is invalid*", "log")
        return redirect("/")
    session["user_id"] = user_in_db.id
    session["first_name"] = user_in_db.first_name
    session["last_name"] = user_in_db.last_name
    return redirect(f"/dashboard/{session['user_id']}")


# Route to render about page
@app.route("/users/about")
def about_us():
    return render_template("about.html")

# Route for logout and clear session


@app.route("/users/logout")
def logout():
    session.clear()
    return redirect("/")

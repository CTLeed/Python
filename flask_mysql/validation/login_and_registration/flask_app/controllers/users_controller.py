from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask_app.models.users_model import User
from flask import flash
import re

bcrypt = Bcrypt(app)

# Route for front page for login and registration


@app.route("/")
def landing():
    return render_template('index.html')


# Route to process registration form
@app.route("/users/reg_process", methods=["POST"])
def register_user():
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
    return redirect("/dashboard")

# Route to process login credentials


@app.route("/users/login_process", methods=["POST"])
def user_log():
    data = {
        'email': request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid credentials", "log")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("*Invalid credentials*", "log")
        return redirect("/")
    session["user_id"] = user_in_db.id
    session["first_name"] = user_in_db.first_name
    return redirect("/dashboard")

# Route to dashboard with verification of successful login


@app.route("/dashboard")
def user_dashboard():
    if not "user_id" in session:
        return redirect("/")
    return render_template("/dashboard.html")

# Route to logout and clear session


@app.route("/users/logout")
def user_logout():
    session.clear()
    return redirect("/")

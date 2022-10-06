from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.users_model import User


@app.route("/")
@app.route("/users")
def main():
    all_users = User.get_all()
    return render_template("index.html", all_users=all_users)


# @app.route("/users")
# def models():
#     return render_template("results.html")

#  Route to render the form for a new user
@app.route("/users/new")
def new_user_form():
    return render_template("new_user.html")

# Route to process creating a new user


@app.route("/users/create", methods=["POST"])
def create_user():
    User.create(request.form)
    return redirect("/")

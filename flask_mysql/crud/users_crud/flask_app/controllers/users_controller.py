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

# route to render a single user info


@app.route("/users/<int:id>")
def get_one_user(id):
    data = {"id": id}
    user = User.get_one(data)
    return render_template("users_one.html", user=user)

# Route to process creating a new user


@app.route("/users/create", methods=["POST"])
def create_user():
    user = User.create(request.form)
    return redirect(f"/users/{user}")


# Route to get render the update form
@app.route("/users/<int:id>/edit")
def edit_user(id):
    data = {"id": id}
    user = User.get_one(data)
    return render_template("user_edit.html", user=user)


@app.route("/users/<int:id>/update", methods=["POST"])
def update_user(id):
    data = {
        **request.form,
        "id": id
    }
    User.update(data)
    return redirect(f"/users/{id}")

# Route to delete user


@app.route("/users/<int:id>/delete")
def delete_user(id):
    data = {"id": id}
    User.delete(data)
    return redirect("/")

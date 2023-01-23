from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask_app.models.recipe_model import Recipe
import re

bcrypt = Bcrypt(app)


@app.route("/recipes")
def show_recipes():
    if not "user_id" in session:
        return redirect("/")
    recipes = Recipe.get_all()
    print(recipes)
    return render_template("user_recipes.html", recipes=recipes)


@app.route("/recipe/new")
def new_recipe():
    if not "user_id" in session:
        return redirect("/")
    return render_template("new_recipe.html")


@app.route("/recipe/create", methods=["POST"])
def create_recipe():
    if "user_id" not in session:
        return redirect("/")
    if not Recipe.validator(request.form):
        return redirect("/recipe/new")
    data = {
        **request.form,
        "user_id": session["user_id"]
    }
    id = Recipe.create(data)
    print(id)
    return redirect(f"/recipe/show/{id}")


@app.route("/recipe/show/<int:id>")
def show_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    recipe = Recipe.get_one({"id": id})
    return render_template("one_recipe.html", recipe=recipe)


@app.route("/recipe/edit/<int:id>")
def edit_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    recipe = Recipe.get_one({"id": id})
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/recipe/update", methods=["POST"])
def update_recipe():
    if "user_id" not in session:
        return redirect("/")
    if not Recipe.validator(request.form):
        id = request.form["id"]
        return redirect(f"/recipe/edit/{id}")
    data = {
        **request.form
    }
    Recipe.update(data)
    return redirect("/recipes")


@app.route("/recipe/delete/<int:id>")
def delete_recipe(id):
    Recipe.delete({"id": id})
    return redirect("/recipes")

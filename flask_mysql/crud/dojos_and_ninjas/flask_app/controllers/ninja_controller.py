from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models import dojo_model


@app.route("/ninjas/new")
def new_ninja():
    all_dojos = dojo_model.Dojo.get_all()
    return render_template("new_ninja.html", all_dojos=all_dojos)


@app.route("/ninjas/create", methods=["POST"])
def createe_ninja():
    print(request.form)
    Ninja.create(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")

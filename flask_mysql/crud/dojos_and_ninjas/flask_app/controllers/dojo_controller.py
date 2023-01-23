from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo
from flask_app.models import ninja_model


# Main route to display list of dojos and add a new one
@app.route("/")
@app.route("/dojos")
def main():
    all_dojos = Dojo.get_all()
    return render_template("index.html", all_dojos=all_dojos)


# Route to get single dojo information with list of Ninjas in that dojo
@app.route("/dojos/<int:id>")
def one_dojo(id):
    data = {"id": id}
    dojo = Dojo.get_one(data)
    return render_template("one_dojo.html", dojo=dojo)


# Route to create a new dojo
@app.route("/dojos/create", methods=["POST"])
def create_model():
    dojo = Dojo.create(request.form)
    return redirect(f"/dojos/{dojo}")

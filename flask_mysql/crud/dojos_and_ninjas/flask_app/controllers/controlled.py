from flask_app import app
from flask import render_template, redirect, request
from models.model import Model


from flask_app.models.dojo_model import Model


@app.route("/")
def main():
    all_models = Model.get_all()
    return render_template("index.html", all_models=all_models)


@app.route("/models")
def models():
    return render_template("results.html")


@app.route("/models/create", methods=["POST"])
def create_model():
    Model.create(request.form)
    return redirect("/models")


@app.route("/models/new")
def new_model_form():
    return render_template("model_new.html")

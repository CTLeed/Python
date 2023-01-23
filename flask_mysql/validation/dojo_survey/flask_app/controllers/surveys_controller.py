import re
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import survey_model


@app.route("/")
def render_survey():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    print(request.form)
    # data = {
    #     'name': request.form["name"],
    #     'location': request.form["location"],
    #     'language': request.form["language"],
    # }
    if not survey_model.Survey.validator(request.form):
        return redirect("/")
    return redirect(f"/result/{survey_model.Survey.add_to_db(request.form)}")


@app.route("/result/<int:id>")
def results(id):
    data = {
        "id": id
    }
    survey = survey_model.Survey.display_survey(data)
    return render_template("results.html", survey=survey)

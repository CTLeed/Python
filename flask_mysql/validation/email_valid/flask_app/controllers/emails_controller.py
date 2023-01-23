from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect, request
from flask import flash
import re
from flask_app.models.email_model import Email
DATABASE = "email_valid_db"


@app.route("/")
def email_form():
    return render_template("index.html")


@app.route("/email/process", methods=["POST"])
def email_process():
    data = {
        "email": request.form["email"]
    }
    print(data['email'])
    if not Email.validator(data["email"]):
        return redirect("/")
    id = Email.create(request.form)
    return redirect(f"/email/display/{id}")


@app.route("/email/display/<int:id>")
def email_success(id):
    emails = Email.get_all()
    new_email = Email.get_one({"id": id})
    return render_template("email_display.html", emails=emails, new_email=new_email)


@app.route("/email/delete/<int:id>")
def email_remove(id):
    Email.delete({"id": id})
    return redirect("/")

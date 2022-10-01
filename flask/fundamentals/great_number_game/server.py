from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "There can be only one"


@app.route("/")
def html_table():
    if "count" not in session:
        session["count"] = 0
    if "number" not in session:
        session["number"] = random.randint(1, 100)
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    session["guess"] = request.form["guess"]
    session["count"] += 1
    if int(session["number"]) < int(session["guess"]):
        session["answer"] = "too high"
        return redirect("/")
    elif int(session["number"]) > int(session["guess"]):
        session["answer"] = "too low"
        return redirect("/")
    else:
        session["answer"] = "correct"
        return redirect("/")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

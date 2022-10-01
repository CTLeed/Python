from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "to infinity and beyond"


@app.route("/")
@app.route("/count")
def counter():
    if "true_count" not in session:
        session["true_count"] = 1
    else:
        session["true_count"] += 1
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    session["click"] = request.form["click"]
    return redirect("/count")


@app.route("/add2", methods=["POST"])
def add2():
    # session["add2"] = request.form["add2"]
    session["count"] += 1
    return redirect("/count")


@app.route("/add_any", methods=["POST"])
def add_any():
    session["add_any"] = request.form["add_any"]
    session["count"] += int(session["add_any"]) - 1
    return redirect("/count")


@app.route("/destroy_session", methods=["POST"])
def destroy_session():
    session.pop("count")
    return redirect("/count")


if __name__ == "__main__":
    app.run(debug=True)

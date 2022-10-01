from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "That's mom's foot"


@app.route("/")
def survey():
    session.clear()
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect("/result")


@app.route("/result")
def results():
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True)

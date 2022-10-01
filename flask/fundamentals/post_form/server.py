from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "There are no secrets on GitHub"


@app.route("/")  # VIEW ROUTE
def html_table():
    return render_template("form.html")


@app.route("/process_form", methods=["POST"])  # ACTION ROUTE
def process_form():
    session["dog_name"] = request.form["dog_name"]
    session["breed"] = request.form["breed"]
    session["age"] = request.form["age"]
    session["cuteness"] = request.form["cuteness"]
    return redirect("/show")
    # return render_template("show.html", results=request.form)


@app.route("/show")
def show():
    return render_template("show.html")


if __name__ == "__main__":
    app.run(debug=True)

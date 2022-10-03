from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "It's the one that says BAD M F'er on it"


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

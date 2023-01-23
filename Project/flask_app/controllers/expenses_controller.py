from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user_model import User
from flask_app.models.expense_model import Expense
from flask_app.models.deposit_model import Deposit


# Route to process expenses


@app.route("/users/process_expense", methods=["POST"])
def process_expense():
    if not "user_id" in session:
        return redirect("/")
    user = User.get_one({"id": session["user_id"]})
    data = {
        **request.form,
        "user_id": user.id
    }
    Expense.insert(data)
    user_balance = user.balance - float(request.form["amount"])
    User.balance_change({"balance": user_balance, "id": user.id})
    print("expense route")
    return redirect("/processing_route")


@app.route("/processing_route")
def process():
    print("process route")
    return redirect(f"/dashboard/{session['user_id']}")


# Route to process deposits
@app.route("/users/process_deposit", methods=["POST"])
def process_deposit():
    if not "user_id" in session:
        return redirect("/")
    user = User.get_one({"id": session["user_id"]})
    data = {
        **request.form,
        "user_id": user.id
    }
    Deposit.insert(data)
    user_balance = user.balance + float(request.form["amount"])
    User.balance_change({"balance": user_balance, "id": user.id})
    return redirect("/processing_route")

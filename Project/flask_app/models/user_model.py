from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import expense_model
from flask_app import DATABASE
import re
ALPHA = re.compile(r"^[a-zA-Z]+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
PHONE = re.compile(
    r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")


# User Class
class User:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.balance = data["balance"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.expenses = []


# Create a new user

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

# Get one user

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users LEFT JOIN expenses ON users.id = expenses.user_id WHERE users.id = %(id)s ORDER BY expenses.created_at DESC, expenses.date;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            user_instance = cls(results[0])
            for each_row in results:
                expense_data = {
                    **each_row,
                    "id": each_row["expenses.id"],
                    "created_at": each_row["expenses.created_at"],
                    "updated_at": each_row["expenses.updated_at"]
                }
                expense_instance = expense_model.Expense(expense_data)
                user_instance.expenses.append(expense_instance)
            return user_instance
        return results

    @classmethod
    def balance_change(cls, data):
        query = "UPDATE users SET balance = %(balance)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            return cls(results[0])
        return False

    @staticmethod
    def validator(incoming_user):
        is_Valid = True
        if len(incoming_user["first_name"]) < 1:
            flash("First name is required", "first_name")
            is_Valid = False
        elif len(incoming_user["first_name"]) < 2:
            flash("First name must be at least 2 letters", "first_name")
            is_Valid = False
        elif not ALPHA.match(incoming_user["first_name"]):
            flash("First name may only contain letters", "first_name")
            is_Valid = False
        if len(incoming_user["last_name"]) < 1:
            flash("Last name is required", "last_name")
            is_Valid = False
        elif len(incoming_user["last_name"]) < 2:
            flash("Last name must be at least 2 letters", "last_name")
            is_Valid = False
        elif not ALPHA.match(incoming_user["last_name"]):
            flash("Last name may only contain letters", "last_name")
            is_Valid = False
        if len(incoming_user["email"]) < 1:
            flash("Email is required", "email")
            is_Valid = False
        elif not EMAIL_REGEX.match(incoming_user["email"]):
            flash("Email must be valid", "email")
        else:
            data = {
                'email': incoming_user["email"]
            }
            user_in_db = User.get_by_email(data)
            if user_in_db:
                flash("Email already registerd", "email")
                is_Valid = False
        if len(incoming_user["password"]) < 8:
            flash("Password must contain at least 8 characters", "password")
            is_Valid = False
        elif incoming_user["password"] != incoming_user["confirm"]:
            flash("Password does not match confirmation", "confirm")
            is_Valid = False
        return is_Valid

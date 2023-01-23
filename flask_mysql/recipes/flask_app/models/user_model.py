from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import recipe_model
from flask_app import DATABASE
import re
ALPHA = re.compile(r"^[a-zA-Z]+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class User:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            user_instance = cls(results[0])
            recipe_list = []
            for each_row in results:
                recipe_data = {
                    **each_row,
                    "id": each_row["recipes.id"],
                    "created_at": each_row["created_at"],
                    "updated_at": each_row["updated_at"]
                }
                recipe_instance = recipe_model.Recipe.create(recipe_data)
                recipe_list.append(recipe_instance)
                user_instance.recipes = recipe_list
                return user_instance
        return results

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
            flash("First name is required", "reg")
            is_Valid = False
        elif len(incoming_user["first_name"]) < 2:
            flash("First name must be at least 2 letters", "reg")
            is_Valid = False
        elif not ALPHA.match(incoming_user["first_name"]):
            flash("First name may only contain letters", "reg")
            is_Valid = False
        if len(incoming_user["last_name"]) < 1:
            flash("Last name is required", "reg")
            is_Valid = False
        if len(incoming_user["last_name"]) < 2:
            flash("Last name must be at least 2 letters", "reg")
            is_Valid = False
        if len(incoming_user["email"]) < 1:
            flash("Email is required", "reg")
            is_Valid = False
        elif not EMAIL_REGEX.match(incoming_user["email"]):
            flash("Email must be valid", "reg")
        else:
            data = {
                'email': incoming_user["email"]
            }
            user_in_db = User.get_by_email(data)
            if user_in_db:
                flash("Email already registerd", "reg")
                is_Valid = False
        if len(incoming_user["password"]) < 8:
            flash("Password must contain at least 8 characters", "reg")
            is_Valid = False
        elif incoming_user["password"] != incoming_user["confirm_password"]:
            flash("Password does not match confirmation", "reg")
            is_Valid = False
        return is_Valid

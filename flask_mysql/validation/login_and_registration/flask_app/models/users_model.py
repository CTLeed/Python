from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app import DATABASE
from flask import flash
import re
ALPHA = re.compile(r"^[a-zA-Z]+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_users = []
        for each_user in results:
            user_instance = cls(each_user)
            all_users.append(user_instance)
        return all_users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

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

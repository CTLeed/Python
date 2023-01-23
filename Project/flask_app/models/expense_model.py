from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user_model
from flask_app import DATABASE
import re
ALPHA = re.compile(r"^[a-zA-Z]+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
NUMBER = re.compile(r"^[0-9]+$")


class Expense:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.payee = data["payee"]
        self.amount = data["amount"]
        self.date = data["date"]
        self.category = data["category"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def insert(cls, data):
        query = "INSERT INTO expenses (payee, amount, date, category, user_id) VALUES (%(payee)s, %(amount)s, %(date)s, %(category)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

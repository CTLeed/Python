from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
DATABASE = "email_valid_db"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        emails_from_db = connectToMySQL(DATABASE).query_db(query)
        all_emails = []
        for each_email in emails_from_db:
            email_instance = cls(each_email)
            all_emails.append(email_instance)
        return all_emails

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM emails WHERE emails.email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM emails WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(potential_email):
        is_Valid = True
        if len(potential_email) < 4:
            flash("That email is not long enough")
            is_Valid = False
        elif not EMAIL_REGEX.match(potential_email):
            flash("That is not a valid email address")
            is_Valid = False
        else:
            email_in_db = Email.get_by_email(potential_email)
            if email_in_db:
                flash("This email is already in use")
        return is_Valid

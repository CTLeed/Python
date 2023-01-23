from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
DATABASE = "dojo_survey_db"

# NAME_REGEX = re.compile()


class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_to_db(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def display_survey(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validator(incoming_survey):
        is_Valid = True
        if len(incoming_survey['name']) < 1:
            flash("Name is required")
            is_Valid = False
        if not 'location' in incoming_survey:
            flash("Location is required")
            is_Valid = False
        if not 'language' in incoming_survey:
            flash("Language is required")
            is_Valid = False
        return is_Valid

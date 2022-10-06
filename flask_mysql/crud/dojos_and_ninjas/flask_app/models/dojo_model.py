from flask_app.models.ninja_model import Ninja
from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "dojos_and_ninjas_schema"


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        return

    # Get all info from table

     @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        dojos_from_db = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for each_dojo in dojos_from_db:
            dojo_instance = cls(each_dojo)
            all_dojos.append(dojo_instance)
        return all_dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            return cls(results[0])
        return False

    # Add info to table
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    #  Update info in table
    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name = %(name)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # Delete info from table

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)


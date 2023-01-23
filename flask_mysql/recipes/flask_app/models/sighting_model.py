from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user_model
from flask_app import DATABASE
import re


class Recipe:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under_30 = data["under_30"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30 = %(under_30)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if len(results) > 0:
            recipe_list = []
            for row_in_db in results:
                recipe_instance = cls(row_in_db)
                user_data = {
                    **row_in_db,
                    "id": row_in_db["users.id"],
                    "created_at": row_in_db["users.created_at"],
                    "updated_at": row_in_db["users.updated_at"]
                }
                user_instance = user_model.User(user_data)
                recipe_instance.maker = user_instance
                recipe_list.append(recipe_instance)
            return recipe_list
        return []

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            recipe_instance = cls(results[0])
            for row_in_db in results:
                user_data = {
                    **row_in_db,
                    "id": row_in_db["users.id"],
                    "created_at": row_in_db["users.created_at"],
                    "updated_at": row_in_db["users.updated_at"]
                }
                user_instance = user_model.User(user_data)
            recipe_instance.maker = user_instance
        return recipe_instance

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(potential_recipe):
        is_Valid = True
        if len(potential_recipe["name"]) < 3:
            flash("A name must be more than 3 characters")
            is_Valid = False
        if len(potential_recipe["description"]) < 3:
            flash("A description must be more than 3 characters")
            is_Valid = False
        if len(potential_recipe["instructions"]) < 3:
            flash("Instructions must be more than 3 characters")
            is_Valid = False
        return is_Valid

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book_model
from flask import flash

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []

    @classmethod
    def create(cls,data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return connectToMySQL('books_schema').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        all_authors = []
        for row in results:
            all_authors.append(cls(row))
        return all_authors
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        print(results)
        if len(results) > 0:
            author = cls(results[0])
            for row in results:
                book_data = {
                    **row,
                    'id' : row['books.id'],
                    'created_at' : row['books.created_at'],
                    'updated_at'  : row['books.updated_at']
                }
                author.favorites.append(book_model.Book(book_data))
                print(author.favorites)
            return author
        return False
    
    @staticmethod
    def validator(data):
        is_valid = True
        if len(data['name']) < 1:
            flash('Name is required')
            is_valid = False
        return is_valid
    
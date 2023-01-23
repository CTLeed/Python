from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author_model

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorited_by = []
    
    @classmethod
    def create(cls,data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        return connectToMySQL('books_schema').query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for row in results:
            books.append(cls(row))
        return books

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        if len(results) > 0:
            book = cls(results[0])
            for row in results:
                author_data = {
                    **row,
                    'id' : row['authors.id'],
                    'created_at' : row['authors.created_at'],
                    'updated_at'  : row['authors.updated_at']
                }
                book.favorited_by.append(author_model.Author(author_data))
            return book
        return False
    
    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data)
    
    @staticmethod
    def validator(data):
        is_valid = True
        if len(data['title']) < 1:
            flash('*Title is required', 'title')
            is_valid = False
        if len(data['num_of_pages']) < 1:
            flash('*Number of pages is required', 'num')
            is_valid = False
        return is_valid
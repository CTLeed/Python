from crypt import methods
from flask_app.models.book_model import Book
from flask_app.models.author_model import Author
from flask_app import app
from flask import request, render_template, redirect

@app.route('/books')
def show_books():
    return render_template("books_show.html", books = Book.get_all())

@app.route('/book/create', methods = ["POST"])
def create_book():
    if not Book.validator(request.form):
        return redirect('/books')
    Book.create(request.form)
    return redirect('/books')

@app.route('/add/favorites/<int:id>', methods = ["POST"])
def add_fav(id):
    data = {
        'author_id' : id,
        **request.form
    }
    Book.add_favorite(data)
    return redirect(f'/author/show/{id}')

@app.route('/book/favorites/<int:id>', methods = ["POST"])
def add_fav_author(id):
    data = {
        'book_id' : id,
        **request.form
    }
    Book.add_favorite(data)
    return redirect(f'/book/show/{id}')

@app.route('/book/show/<int:id>')
def show_book(id):
    book = Book.get_one({'id': id})
    author_ids = []
    for author in book.favorited_by:
        author_ids.append(author.id)
    return render_template("book_one.html", book = book , authors = Author.get_all(), author_ids = author_ids)
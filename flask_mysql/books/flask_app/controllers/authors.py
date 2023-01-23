from flask_app.models.author_model import Author
from flask_app.models.book_model import Book
from flask_app import app
from flask import request, render_template, redirect

@app.route('/')
def show_authors():
    return render_template("authors_show.html", authors = Author.get_all())

@app.route('/author/create', methods = ["POST"])
def create_author():
    if not Author.validator(request.form):
        return redirect('/')
    Author.create(request.form)
    return redirect('/')

@app.route('/author/show/<int:id>')
def show_author(id):
    author = Author.get_one({'id' : id})
    book_ids = []
    for book in author.favorites:
        book_ids.append(book.id)
    return render_template("author_one.html", author = author, books = Book.get_all(), book_ids = book_ids)

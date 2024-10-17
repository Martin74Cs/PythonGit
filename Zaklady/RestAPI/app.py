# pip install Flask
# pip install SQLAlchemy
# pip install Flask-SQLAlchemy
# pip install Flask-Migrate
# pip install Flask SQLAlchemy Flask-Migrate

# pip install export 
# export FLASK_APP=RestApi.py  # Na Windows použijte `set FLASK_APP=app.py`
# flask db init
# flask db migrate -m "Initial migration."
# flask db upgrade

import os
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Renderování Šablon render_template
from data import db
from models import Author, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializace SQLAlchemy a Migrate
# Inicializace SQLAlchemy a Flask-Migrate
# db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

# Import modelů po inicializaci db, aby se zabránilo kruhovým importům
# from models import Author, Book

# Vytvoření databáze a tabulky
# @app.before_first_request
# @app.before_request
# def create_tables():
#     db.create_all()
#     print("Data vytvořena")

# Ukázková data
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"},
]

@app.route('/api/data', methods=['GET'])
def GetBooks():
    return jsonify(books)

# Získání knihy podle ID
@app.route('/api/data/<int:book_id>', methods=['GET'])
def GetBook(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Kniha nenalezena"}), 404

# Vytvoření nové knihy
@app.route('/api/data', methods=['POST'])
def CreateBook():
    new_book = request.get_json()
    new_book["id"] = books[-1]["id"] + 1 if books else 1
    books.append(new_book)
    return jsonify(new_book), 201

# Aktualizace knihy
@app.route('/api/data/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    return jsonify({"error": "Kniha nenalezena"}), 404

# Smazání knihy
@app.route('/api/data/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Kniha smazána"}), 200





# API Endpoint pro získání všech knih včetně informací o autorech
@app.route('/api/books', methods=['GET'])
def GetData():
    records = Book.query.all()
    return jsonify([record.to_dict() for record in records]), 200

# Vytvoření nové knihy
@app.route('/api/books', methods=['POST'])
def CreateData():
    new_record = request.get_json()
    record = Book(      
        title=new_record.get('title'),
        author=new_record.get('author'),
        year=new_record.get('year')  
    )
    db.session.add(record)
    db.session.commit()
    return jsonify(record.to_dict()), 201

# API Endpoint pro získání všech autorů
@app.route('/api/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return jsonify([author.to_dict() for author in authors])

# endpoint, který vrací autory spolu s jejich knihami.
@app.route('/api/authors_with_books', methods=['GET'])
def get_authors_with_books():
    authors = Author.query.all()
    authors_data = []
    for author in authors:
        author_dict = author.to_dict()
        author_dict['books'] = [book.to_dict() for book in author.books]
        authors_data.append(author_dict)
    return jsonify(authors_data)

# API Endpoint pro přidání nového autora
@app.route('/api/authors', methods=['POST'])
def add_author():
    data = request.get_json()
    if not data or not 'name' in data:
        return jsonify({"error": "Nedostatek dat"}), 400
    
    # Kontrola existence autora
    if Author.query.filter_by(name=data['name']).first():
        return jsonify({"error": "Autor již existuje"}), 400
    
    new_author = Author(
        name=data['name'],
        biography=data.get('biography')
    )
    db.session.add(new_author)
    db.session.commit()
    return jsonify(new_author.to_dict()), 201

# API Endpoint pro přidání nové knihy
@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.get_json()
    required_fields = ['title', 'author_id', 'year', 'genre']
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Nedostatek dat"}), 400
    
    # Kontrola existence autora
    author = Author.query.get(data['author_id'])
    if not author:
        return jsonify({"error": "Autor nenalezen"}), 404
    
    new_book = Book(
        title=data['title'],
        author_id=data['author_id'],
        year=data['year'],
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

# Šablona pro zobrazení knih v HTML
@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', books=books)

# Šablona pro zobrazení knih v HTML
@app.route('/addbook')
def addbook():
    books = Book.query.all()
    return render_template('addbook.html', books=books)

if __name__ == '__main__':
    os.system("cls")
    print("Konec Ctrl+C")
    
    # # Vytvoření autorů
    # author1 = Author(name="George Orwell", biography="Anglický spisovatel známý pro dystopické romány.")
    # author2 = Author(name="Aldous Huxley", biography="Anglický spisovatel známý pro sci-fi romány.")
    # author3 = Author(name="Ray Bradbury", biography="Americký spisovatel známý pro dystopické a sci-fi příběhy.")
    # print("Autor")
    # # Přidání autorů do session
    # db.session.add_all([author1, author2, author3])
    # db.session.commit()
    # print("Autor")

    app.run(debug=True)
    # app.run(debug=False)

# Nainstalujte Flask a Gunicorn:
# pip install Flask gunicorncl

# Nakonec vytvořte requirements.txt:
# pip freeze > requirements.txt

#  http://127.0.0.1
# gunicorn --bind 0.0.0.0:8000 app:app

# upraveno 
# gunicorn --bind 127.0.0.1:8000 app:app

# jen test instalace
# pip install gunicorn

# jiny server -  nastala chyba
# pip install uwsgi


# pip install Flask waitress
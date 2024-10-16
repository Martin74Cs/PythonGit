# app.py
from flask import Flask, jsonify, request, render_template
from flask_migrate import Migrate
from data import db
from models import Author, Book

app = Flask(__name__)

# Konfigurace databáze - SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializace SQLAlchemy a Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)

# API Endpointy

# Získání všech knih
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# Přidání nové knihy
@app.route('/books', methods=['POST'])
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
        genre=data['genre'],
        isbn=data.get('isbn'),
        pages=data.get('pages')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

# Získání všech autorů
@app.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return jsonify([author.to_dict() for author in authors])

# Přidání nového autora
@app.route('/authors', methods=['POST'])
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

# Získání autorů s jejich knihami
@app.route('/authors_with_books', methods=['GET'])
def get_authors_with_books():
    authors = Author.query.all()
    authors_data = []
    for author in authors:
        author_dict = author.to_dict()
        author_dict['books'] = [book.to_dict() for book in author.books]
        authors_data.append(author_dict)
    return jsonify(authors_data)

# Šablona pro zobrazení knih v HTML
@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)

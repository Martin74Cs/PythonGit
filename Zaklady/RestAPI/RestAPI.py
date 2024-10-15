# pip install Flask
# pip install SQLAlchemy
# pip install Flask-SQLAlchemy
# pip install Flask-Migrate

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # data = db.Column(db.JSON, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
        }

# Vytvoření databáze a tabulky
# @app.before_first_request
@app.before_request
def create_tables():
    db.create_all()
#     print("Data vytvořena")

# Ukázková data
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"},
]

# Získání všech knih
@app.route('/api/books', methods=['GET'])
def GetBooks():
    return jsonify(books)

@app.route('/api/data', methods=['GET'])
def GetData():
    records = Record.query.all()
    return jsonify([record.to_dict() for record in records]), 200

# Získání knihy podle ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def GetBook(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Kniha nenalezena"}), 404

# Vytvoření nové knihy
@app.route('/api/data', methods=['POST'])
def CreateData():
    new_record = request.get_json()
    record = Record(      
        title=new_record.get('title'),
        author=new_record.get('author')
    )
    db.session.add(record)
    db.session.commit()
    return jsonify(record.to_dict()), 201

# Vytvoření nové knihy
@app.route('/api/books', methods=['POST'])
def CreateBook():
    new_book = request.get_json()
    new_book["id"] = books[-1]["id"] + 1 if books else 1
    books.append(new_book)
    return jsonify(new_book), 201

# Aktualizace knihy
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    return jsonify({"error": "Kniha nenalezena"}), 404

# Smazání knihy
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Kniha smazána"}), 200

if __name__ == '__main__':
    print("Konec Ctrl+C")
    # app.run(debug=True)
    app.run(debug=False)

# Nainstalujte Flask a Gunicorn:
# pip install Flask gunicorn

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
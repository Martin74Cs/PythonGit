# pip install Flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# Ukázková data
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"},
]

# Získání všech knih
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Získání knihy podle ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Kniha nenalezena"}), 404

# Vytvoření nové knihy
@app.route('/api/books', methods=['POST'])
def create_book():
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
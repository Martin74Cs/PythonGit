# models.py
from data import db

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    biography = db.Column(db.Text, nullable=True)
    
    books = db.relationship('Book', backref='author', lazy=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "biography": self.biography
        }

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    isbn = db.Column(db.String(20), nullable=True)
    pages = db.Column(db.Integer, nullable=True)
    
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "isbn": self.isbn,
            "pages": self.pages,
            "author": {
                "id": self.author.id,
                "name": self.author.name
            # "author": self.author.to_dict()  # Vložení informací o autorovi
            # pokud potřebuji jen některé informace o autorovi
            # "author": {
            #     "id": self.author.id,
            #     "name": self.author.name     
            }
        }




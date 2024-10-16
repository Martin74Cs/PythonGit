# populate.py
from app import app, db
from models import Author, Book

with app.app_context():
    # Vytvoření autorů
    author1 = Author(name="George Orwell", biography="Anglický spisovatel známý pro dystopické romány.")
    author2 = Author(name="Aldous Huxley", biography="Anglický spisovatel známý pro sci-fi romány.")
    author3 = Author(name="Ray Bradbury", biography="Americký spisovatel známý pro dystopické a sci-fi příběhy.")
    
    # Přidání autorů do session
    db.session.add_all([author1, author2, author3])
    db.session.commit()
    
    # Vytvoření knih
    book1 = Book(
        title="1984",
        year=1949,
        genre="Dystopie",
        isbn="978-0451524935",
        pages=328,
        author_id=author1.id
    )
    
    book2 = Book(
        title="Brave New World",
        year=1932,
        genre="Sci-Fi",
        isbn="978-0060850524",
        pages=288,
        author_id=author2.id
    )
    
    book3 = Book(
        title="Fahrenheit 451",
        year=1953,
        genre="Sci-Fi",
        isbn="978-1451673319",
        pages=194,
        author_id=author3.id
    )
    
    # Přidání knih do session
    db.session.add_all([book1, book2, book3])
    db.session.commit()
    
    print("Data byla úspěšně přidána do databáze.")

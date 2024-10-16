# Nastavení FLASK_APP
# Na Windows:
set FLASK_APP=app.py
# Na Unix/Linux/macOS:
export FLASK_APP=app.py

# Inicializace migrací
flask db init

# Vytvoření migračního skriptu
flask db migrate -m "Initial migration."

# Aplikace migrací do databáze
flask db upgrade

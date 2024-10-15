# pip install Flask-JWT-Extended
# pip install Flask-limiter
# pip install Flask-marshmallow

# Použijeme knihovnu Werkzeug pro hashování hesel.

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from marshmallow import Schema, fields, validate, ValidationError
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
# Konfigurace databáze SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Konfigurace JWT
app.config['JWT_SECRET_KEY'] = 'váš_tajný_klíč'  # Změňte na silný tajný klíč

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
CORS(app)

# Logování
if not app.debug:
    handler = RotatingFileHandler('error.log', maxBytes=100000, backupCount=3)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)

# Model User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }
    
# Model Record
class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "data": self.data,
            "name": self.name,
            "email": self.email
        }

# Schéma pro validaci dat
class RecordSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    data = fields.Dict(required=True, validate=lambda x: len(x) > 0)

record_schema = RecordSchema()

# Dekorátor pro role-based access
def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            if not user or user.role != role:
                return jsonify({"error": "Forbidden"}), 403
            return f(*args, **kwargs)
        return decorated
    return decorator

# @app.before_first_request
@app._got_first_request
def create_tables():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Uživatelské jméno již existuje"}), 400
    
    new_user = User(username=username)
    new_user.set_password(password)  # V praxi hesla hashujte!
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

@app.route('/api/data', methods=['POST'])
@jwt_required()
@limiter.limit("10 per minute")
def add_data():
    try:
        new_record = record_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Kontrola duplicity emailu
    if Record.query.filter_by(email=new_record['email']).first():
        return jsonify({"error": "Email již existuje"}), 400
    
    record = Record(
        data=new_record['data'],
        name=new_record['name'],
        email=new_record['email']
    )
    db.session.add(record)
    db.session.commit()
    return jsonify(record.to_dict()), 201

@app.route('/api/data', methods=['GET'])
@jwt_required()
def get_data():
    current_user_id = get_jwt_identity()
    # Implementujte logiku pro získání dat spojených s uživatelem
    return jsonify({"data": "secured data"}), 200

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(error="Too many requests, please try again later."), 429

# Pokud chcete umožnit přístup k API pouze prostřednictvím API klíčů, můžete implementovat kontrolu API klíče ve vašich endpointů.
API_KEYS = {"váš_api_klíč"}

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if api_key not in API_KEYS:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/api/data', methods=['POST'])
@require_api_key
def add_data_with_api_key():
    # Vaše logika
    pass

# Omezení Přístupu na Specifické Endpointy
# Používejte role-based access control (RBAC) pro řízení, které uživatelé mají přístup k určitým částem API.
def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            if user.role != role:
                return jsonify({"error": "Forbidden"}), 403
            return f(*args, **kwargs)
        return decorated
    return decorator

@app.route('/admin/data', methods=['POST'])
@jwt_required()
@role_required('admin')
def add_admin_data():
    # Logika pro admin
    pass

# Implementujte logování a monitorování, abyste mohli sledovat a reagovat na bezpečnostní události.
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    handler = RotatingFileHandler('error.log', maxBytes=100000, backupCount=3)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)

if __name__ == '__main__':
    app.run(debug=True)

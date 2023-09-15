from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    date_birth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    consent_processing = db.Column(db.Boolean, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def encrypt_password(self, password):
        self.password = generate_password_hash(password)

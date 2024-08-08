"""Contains the database models"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import JSON

db = SQLAlchemy()

class User(db.Model):
    """User Model that defines the SQL db"""
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    preferences = db.Column(JSON, nullable=True)
    previous_calls = db.Column(JSON, nullable=True)
    accounts = db.Column(JSON, nullable=True)
    audio_path = db.Column(db.String(255), nullable=True)
    transcript_path = db.Column(db.String(255), nullable=True)
    sol_path = db.Column(db.String(255), nullable=True)
    category_path = db.Column(db.String(255), nullable=True)
    summary_path = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f'<User {self.firstname} {self.lastname}>'

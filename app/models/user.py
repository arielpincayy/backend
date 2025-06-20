from app import db
from datetime import datetime, timezone

# Modelo Usuario
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'
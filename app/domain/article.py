"""Domain Article class"""
import datetime
from api import db


class User(db.Model):
    """User Model class"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True)
    content = db.Column(db.Text)
    published_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship("User")

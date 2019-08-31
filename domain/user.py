"""Domain User class"""
import enum
from api import db


class UserStatus(enum.Enum):
    """Status Enum"""
    ACTIVE = enum.auto()
    INACTIVE = enum.auto()


class UserRole(enum.Enum):
    """Role Enum"""
    BASIC = enum.auto()
    ADMIN = enum.auto()


class User(db.Model):
    """User Model class"""
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(256), index=True)
    email = db.Column(db.String(256), index=True)
    password = db.Column(db.String(128))
    status = db.Column(db.Enum(UserStatus))
    role = db.Column(db.Enum(UserRole))

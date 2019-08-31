"""Domain User class"""
import enum
from marshmallow_enum import EnumField
from app.setup import DB, MA

class UserStatus(enum.Enum):
    """Status Enum"""
    ACTIVE = enum.auto()
    INACTIVE = enum.auto()


class UserRole(enum.Enum):
    """Role Enum"""
    BASIC = enum.auto()
    ADMIN = enum.auto()


class User(DB.Model):
    """User Model class"""
    id = DB.Column(DB.BigInteger, primary_key=True, autoincrement=True)
    full_name = DB.Column(DB.String(256), index=True)
    email = DB.Column(DB.String(256), index=True)
    password = DB.Column(DB.String(128))
    status = DB.Column(DB.Enum(UserStatus))
    role = DB.Column(DB.Enum(UserRole))

class UserSchema(MA.ModelSchema):
    """Serialization schema"""
    status = EnumField(UserStatus)
    role = EnumField(UserRole)
    class Meta:
        """Model initialization"""
        model = User

RECORD_SCHEMA = UserSchema()
RECORD_LIST_SCHEMA = UserSchema(many=True)

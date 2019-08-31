"""Domain Article class"""
import datetime
from app.setup import DB, MA
# pylint:disable=unused-import
from app.domain.user import User


class Article(DB.Model):
    """Article Model class"""
    id = DB.Column(DB.BigInteger, primary_key=True,autoincrement=True)
    title = DB.Column(DB.String(256), index=True)
    content = DB.Column(DB.Text)
    published_date = DB.Column(DB.DateTime, default=datetime.datetime.utcnow)
    author_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable=False)
    author = DB.relationship("User")


class ArticleSchema(MA.ModelSchema):
    """Serialization schema"""
    class Meta:
        """Model initialization"""
        model = Article


ARTICLE_SCHEMA = ArticleSchema()
ARTICLE_LIST_SCHEMA = ArticleSchema(many=True)

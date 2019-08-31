"""REST Controller for Article"""
from flask import jsonify, request
from flask_restful import Resource
from app.domain.article import Article, ARTICLE_LIST_SCHEMA, ARTICLE_SCHEMA
from app.setup import REST, DB


class AllRecordsAPI(Resource):
    """API for /article"""

    def get(self):
        """Get all Articles"""
        articles = Article.query.all()
        result = ARTICLE_LIST_SCHEMA.dump(articles)
        return jsonify(result)

    def post(self):
        """Add new Article"""
        new_article = ARTICLE_SCHEMA.load(request.json())
        DB.session.add(new_article)


class SingleRecordAPI(Resource):
    """API for /article/:id"""

    def get(self, article_id):
        """GET single article by id"""
        article = Article.query.filter_by(id=article_id).first_or_404()
        result = ARTICLE_SCHEMA.dump(article)
        return jsonify(result)

    def put(self, article_id):
        """UPDATE article"""
        article = Article.query.filter_by(id=article_id).first_or_404()
        article.update(ARTICLE_SCHEMA.load(request.json()))
        DB.session.commit()
        result = ARTICLE_SCHEMA.dump(article)
        return jsonify(result)


REST.add_resource(AllRecordsAPI, '/article', endpoint = "all_articles")
REST.add_resource(SingleRecordAPI, '/article/<int:article_id>', endpoint = "article_by_id")

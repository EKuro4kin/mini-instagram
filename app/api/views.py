import logging

from flask import Blueprint, request, jsonify

from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

api_blueprint = Blueprint('api_blueprint', __name__)


# Создаем DAO
posts_dao = PostsDAO("./data/posts.json")
comments_dao = CommentsDAO("./data/comments.json")

logger = logging.getLogger("basic")

@api_blueprint.route('/api/posts/')
def page_posts_api_all():
    logger.debug("Запрошены все посты через API")
    posts = posts_dao.get_posts_all()
    return jsonify(posts)

@api_blueprint.route('/api/posts/<int:post_pk>/')
def page_save_posts_to_json(post_pk):
    logger.debug(f"Запрошен пост c pk {post_pk} через API")
    post = posts_dao.get_post_by_pk(post_pk)
    return jsonify(post)
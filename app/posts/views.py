import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request, abort
from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

# Создаем блупринт
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")

# Создаем DAO
posts_dao = PostsDAO("./data/posts.json")
comments_dao = CommentsDAO("./data/comments.json")

logger = logging.getLogger("basic")

# Создаем вьюшку главной страницы со всеми постами
@posts_blueprint.route('/')
def page_posts_all():

    logger.debug("Запрошены все посты")
    try:
        posts = posts_dao.get_posts_all()
        return render_template("index.html", posts=posts)

    except:
        return "Ошибка при выводе постов"

# Создаем вьюшку с выводом конкретного поста и комментариями к нему
@posts_blueprint.route('/posts/<int:post_pk>')
def post_by_pk(post_pk):

    logger.debug(f"Запрошен пост {post_pk}")
    try:
        post = posts_dao.get_post_by_pk(post_pk)
        comments = comments_dao.get_comments_by_post_id(post_pk)
    except (JSONDecodeError, FileNotFoundError) as error:
        return render_template("error.html", error=error)
    except BaseException as error:
        return render_template("error.html", error="Неизвестная ошибка")

    else:
        if post is None:
            abort(404)

        count_comments = len(comments)
        return render_template("post.html", post=post, comments=comments, count_comments=count_comments)

@posts_blueprint.errorhandler(404)
def post_error(e):
    return "Такой пост не найден", 404


# Создаем вьюшку с поиском по маршруту
@posts_blueprint.route('/search/<query>')
def page_search_for_posts(query):
    try:
        filter_posts_for_query = posts_dao.get_search_for_posts(query)
        count_posts = len(filter_posts_for_query)
        return render_template("search.html", posts=filter_posts_for_query, query=query, count_posts=count_posts)
    except:
        return "вы не ввели слово для фильтрации постов либо такого слова нет"

# Создаем вьюшку с выводом пользователя по имени
@posts_blueprint.route('/users/<username>')
def page_posts_by_user(username):
    try:
        filter_user_posts = posts_dao.get_posts_by_user(username)
        return render_template("user-feed.html", posts=filter_user_posts)
    except:
        return "такого пользователя нет"





